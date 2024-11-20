import os
import openai
import json
from app.db.models import SubGoal, Course, Section, Exercise
from sqlalchemy.orm import Session


class ProjectAnalyzer:
    def __init__(self, openai_api_key: str):
        openai.api_key = openai_api_key

    def classify_input(self, user_input: str) -> str:
        prompt = f"Catégorise l'intention suivante dans l'une de ces catégories : 'Finance', 'Santé', 'Éducation', 'Business', 'Autre'. Intention : '{user_input}'"
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo", prompt=prompt, max_tokens=5, temperature=0
            )
            category = response.choices[0].text.strip()
            return category
        except openai.error.OpenAIError as e:
            print(f"Erreur lors de la classification : {e}")
            return "Autre"

    def analyze_project(
        self,
        project_description: str,
        db: Session,
        project_id: int,
        is_premium: bool = False,
    ) -> dict:
        print("Validation de la description du projet...")
        if not self._is_valid_description(project_description):
            raise ValueError(
                "La description du projet doit contenir entre 10 et 1000 caractères."
            )

        print(
            f"Analyse du projet avec le modèle {'gpt-4' if is_premium else 'gpt-3.5-turbo'}..."
        )
        model = "gpt-4" if is_premium else "gpt-3.5-turbo"
        prompt = f"""
        The following is a description of a project: {project_description}
        Please decompose this project into a list of sub-goals that represent a structured learning path.
        Each sub-goal should be an essential step in mastering the skills and knowledge needed to complete the project,
        similar to how a teacher or coach would guide a student. For each sub-goal, provide:
        1. A brief description of what will be learned or achieved.
        2. The skills that will be developed during this step.
        3. Any prerequisite knowledge or previous sub-goals required before starting this sub-goal.

        For **only the first sub-goal**, provide a sample section that will help the user achieve the goal, along with at least one exercise.

        The response should be in the following JSON format:
        [
            {{
                "title": "Sub-goal title",
                "description": "Brief description of what will be learned or achieved",
                "skills": [
                    {{
                        "name": "Skill name",
                        "description": "Skill description"
                    }}
                ],
                "prerequisites": [
                    "Previous sub-goal title (if any)"
                ],
                "section": {{
                    "title": "Section title",
                    "content": "Section content description",
                    "exercises": [
                        {{
                            "question": "Exercise question",
                            "answer": "Exercise answer"
                        }}
                    ]
                }}
            }},
            ...
        ]
        """
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an assistant that helps in project planning.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1500,
                temperature=0.7,
            )
            response_content = response.choices[0].message["content"]
            print("Réponse brute de l'API OpenAI:", response_content)
            sub_goals = self.parse_response(response_content)
        except openai.error.OpenAIError as e:
            raise RuntimeError(f"Failed to analyze project with OpenAI API: {str(e)}")

        self._save_sub_goals_and_courses_to_db(sub_goals, db, project_id)
        difficulty_level = self._evaluate_difficulty(sub_goals)
        feasibility = self._check_feasibility(sub_goals)

        return {
            "sub_goals": sub_goals,
            "difficulty_level": difficulty_level,
            "feasibility": feasibility,
        }

    def parse_response(self, response: str) -> list:
        print("Parsing de la réponse pour extraire les sous-objectifs...")
        response = response.strip().strip("```json").strip("```").strip()
        try:
            sub_goals = json.loads(response)
            for sub_goal in sub_goals:
                sub_goal.setdefault("prerequisites", [])
            print("Sous-objectifs extraits avec succès:", sub_goals)
        except json.JSONDecodeError:
            print("Erreur lors du parsing de la réponse JSON.")
            sub_goals = []

        return sub_goals

    def _save_sub_goals_and_courses_to_db(
        self, sub_goals: list, db: Session, project_id: int
    ):
        print(
            f"Sauvegarde de {len(sub_goals)} sous-objectifs et cours pour le projet {project_id}..."
        )
        for index, sub_goal_data in enumerate(sub_goals):
            new_sub_goal = SubGoal(
                title=sub_goal_data["title"],
                description=sub_goal_data["description"],
                prerequisites=json.dumps(sub_goal_data.get("prerequisites", [])),
                project_id=project_id,
                is_unlocked=(True if index == 0 else False),
            )
            db.add(new_sub_goal)
            db.commit()
            db.refresh(new_sub_goal)

            if index == 0:
                # Générer et sauvegarder le premier cours
                self.generate_course_for_subgoal(
                    new_sub_goal, sub_goal_data, db, project_id
                )
            else:
                # Ne pas générer les cours pour les autres sous-objectifs pour le moment
                pass

        db.commit()
        print("Les sous-objectifs et le premier cours ont été sauvegardés avec succès.")

    def generate_course_for_subgoal(
        self, sub_goal: SubGoal, sub_goal_data: dict, db: Session, project_id: int
    ):
        section_data = sub_goal_data.get("section", {})
        if section_data:
            new_course = Course(
                title=section_data.get("title", "Untitled Course"),
                description=section_data.get("content", ""),
                project_id=project_id,
                subgoal_id=sub_goal.id,
            )
            db.add(new_course)
            db.commit()
            db.refresh(new_course)

            new_section = Section(
                title=section_data.get("title", "Untitled Section"),
                content=section_data.get("content", ""),
                course_id=new_course.id,
            )
            db.add(new_section)
            db.commit()
            db.refresh(new_section)

            for exercise_data in section_data.get("exercises", []):
                new_exercise = Exercise(
                    question=exercise_data["question"],
                    answer=exercise_data["answer"],
                    section_id=new_section.id,
                )
                db.add(new_exercise)
            db.commit()
        else:
            print(f"Aucune section trouvée pour le sous-objectif '{sub_goal.title}'.")

    def _is_valid_description(self, description: str) -> bool:
        return isinstance(description, str) and 10 <= len(description) <= 1000

    def _evaluate_difficulty(self, sub_goals: list) -> int:
        print("Évaluation de la difficulté du projet...")
        num_sub_goals = len(sub_goals)
        has_advanced_skills = any(
            "advanced" in skill.get("description", "").lower()
            for sub_goal in sub_goals
            for skill in sub_goal.get("skills", [])
        )

        if num_sub_goals <= 3 and not has_advanced_skills:
            return 1  # Facile
        elif 4 <= num_sub_goals <= 6:
            return 2  # Intermédiaire
        else:
            return 3  # Difficile

    def _check_feasibility(self, sub_goals: list) -> bool:
        print("Vérification de la faisabilité du projet...")
        estimated_time = 0
        for sub_goal in sub_goals:
            for skill in sub_goal.get("skills", []):
                time_to_learn = skill.get("time_to_learn", 0)
                estimated_time += time_to_learn

        return estimated_time < 200
