import openai
from sqlalchemy.orm import Session
import json
from app.db.models import Course, Section, Exercise, SubGoal


class CourseService:
    def __init__(self, openai_api_key: str):
        openai.api_key = openai_api_key

    def generate_course_from_subgoal(
        self, sub_goal: SubGoal, db: Session, project_id: int
    ):
        # Générer le cours pour le sous-objectif
        course = Course(
            title=sub_goal.title,
            description=sub_goal.description,
            project_id=project_id,
            subgoal_id=sub_goal.id,
        )
        db.add(course)
        db.commit()
        db.refresh(course)

        # Générer les sections et les exercices
        lesson_sections = self.generate_detailed_lessons(sub_goal.title)
        for section in lesson_sections:
            section_instance = Section(
                title=section["title"],
                content=section["content"],
                course_id=course.id,
            )
            db.add(section_instance)
            db.commit()
            db.refresh(section_instance)

            for exercise_data in section["exercises"]:
                exercise = Exercise(
                    question=exercise_data["question"],
                    answer=exercise_data["answer"],
                    section_id=section_instance.id,
                )
                db.add(exercise)
            db.commit()

    def generate_detailed_lessons(self, subgoal_title: str) -> list:
        """Génère des sections détaillées pour un sous-objectif."""
        sections = []
        section_types = [
            "introduction",
            "main concepts",
            "examples",
            "advanced concepts",
            "practical applications",
            "summary",
        ]
        for section_type in section_types:
            section_content = ""
            for _ in range(3):
                section = self.generate_section(subgoal_title, section_type)
                if section:
                    section_content += section["content"] + "\n"
                else:
                    print(
                        f"Erreur lors de la génération de la section '{section_type}'."
                    )
                    continue

            consolidated_section = {
                "title": section_type.capitalize(),
                "content": section_content.strip(),
                "exercises": self.generate_multiple_exercises(
                    subgoal_title, section_type
                ),
            }
            sections.append(consolidated_section)

        return sections

    def generate_section(self, subgoal_title: str, section_type: str) -> dict:
        """Génère une section spécifique pour un sous-objectif."""
        prompt = f"""
        Create a detailed {section_type} for the sub-goal: "{subgoal_title}". 
        Include comprehensive explanations and examples, and create 3 exercises to test understanding.
        Format the response as follows:
        {{
            "title": "{section_type.capitalize()}",
            "content": "Detailed explanation of {section_type}",
            "exercises": [
                {{
                    "question": "Exercise question",
                    "answer": "Correct answer"
                }},
                ...
            ]
        }}
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a highly skilled teacher creating detailed lessons.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=3500,
                temperature=0.7,
            )

            return self.parse_lesson_response(response.choices[0].message["content"])

        except openai.error.OpenAIError as e:
            print(f"Erreur lors de la génération de la section '{section_type}': {e}")
            return {}

    def parse_lesson_response(self, response_content: str) -> dict:
        """Parse la réponse pour extraire une section de cours et ses exercices."""
        try:
            section_data = json.loads(response_content)
            return section_data
        except json.JSONDecodeError:
            print("Erreur lors du parsing de la réponse JSON.")
            return {}

    def generate_multiple_exercises(
        self, subgoal_title: str, section_type: str
    ) -> list:
        """Génère plusieurs exercices pour une section donnée."""
        exercises = []
        for i in range(3):
            prompt = f"Create exercise {i+1} for the {section_type} section of the sub-goal: {subgoal_title}. Include both a question and a correct answer."
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a teacher creating exercises.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                    max_tokens=300,
                )

                content = response.choices[0].message["content"]
                question, answer = self.parse_exercise_response(content)
                exercises.append({"question": question, "answer": answer})

            except openai.error.OpenAIError as e:
                print(f"Erreur lors de la génération de l'exercice {i+1}: {e}")
                continue

        return exercises

    def parse_exercise_response(self, content: str) -> tuple:
        """Parse le contenu d'un exercice pour obtenir question et réponse."""
        try:
            question, answer = content.split("Answer:")
            return question.strip(), answer.strip()
        except ValueError:
            print("Erreur lors du parsing de la réponse d'exercice.")
            return "Erreur de question", "Erreur de réponse"
