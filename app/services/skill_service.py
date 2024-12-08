from sqlalchemy.orm import Session
from app.db.models import Skill, Project
from app.schemas.skill_schemas import SkillCreate
import openai
import logging


class SkillService:
    @staticmethod
    def create_skill(db: Session, skill_data: SkillCreate) -> Skill:
        """
        Crée une compétence dans l'arbre.
        """
        new_skill = Skill(**skill_data.dict())
        db.add(new_skill)
        db.commit()
        db.refresh(new_skill)
        return new_skill

    @staticmethod
    def generate_skills_with_ai(
        db: Session,
        project_id: int,
        user_data: dict,
        openai_api_key="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",
        is_premium=True,
    ) -> list:
        """
        Génère des compétences pour un projet à l'aide d'une IA.
        """
        # Récupérer le projet
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise ValueError("Project not found.")

        # Configurez l'API OpenAI
        openai.api_key = openai_api_key

        # Définir le prompt pour l'IA
        prompt = f"""
        Vous êtes un assistant en gestion de projet. Créez un arbre de compétences pour le projet suivant :
        Nom : {project.name}
        Description : {project.description}

        Données utilisateur :
        - Poids cible : {user_data['goal_weight']} kg
        - Poids actuel : {user_data['current_weight']} kg
        - Apport calorique quotidien : {user_data['daily_calories']}
        - Niveau d'exercice : {user_data['exercise_level']}
        - Durée : {user_data['duration']} jours

        Structurez les compétences en un arbre hiérarchique avec des liens logiques.
        Chaque compétence doit inclure :
        - Un nom
        - Une description
        - Un niveau de difficulté (facile, modéré, difficile)
        - Les dépendances éventuelles avec d'autres compétences

        Limitez à 5 compétences principales pour les comptes gratuits et 10 pour les comptes premium.
        """

        model = "gpt-4" if is_premium else "gpt-3.5-turbo"

        try:
            # Appeler l'IA pour générer les compétences
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "system", "content": prompt}],
                max_tokens=1000,
                temperature=0.7,
            )
            generated_skills = response.choices[0].message.content.strip()
            logging.info(f"Compétences générées par l'IA : {generated_skills}")

            # Transformer le texte généré en objets Skill
            skills = SkillService._parse_generated_skills(
                db, project_id, generated_skills
            )
            return skills

        except Exception as e:
            raise ValueError(f"Erreur lors de la génération des compétences : {str(e)}")

    @staticmethod
    def _parse_generated_skills(
        db: Session, project_id: int, generated_skills: str
    ) -> list:
        """
        Transforme le texte généré par l'IA en objets Skill.
        """
        try:
            # Supposons que l'IA génère un JSON structuré
            skills_data = eval(generated_skills)
            created_skills = []

            for skill_data in skills_data:
                new_skill = Skill(
                    name=skill_data["name"],
                    description=skill_data["description"],
                    difficulty_level=skill_data["difficulty_level"],
                    project_id=project_id,
                    parent_id=skill_data.get("parent_id"),  # Optionnel si hiérarchie
                )
                db.add(new_skill)
                db.commit()
                db.refresh(new_skill)
                created_skills.append(new_skill)

            return created_skills
        except Exception as e:
            raise ValueError(
                f"Erreur lors de l'analyse des compétences générées : {str(e)}"
            )

    @staticmethod
    def get_skills_for_project(db: Session, project_id: int) -> list:
        """
        Récupère toutes les compétences pour un projet, organisées en arbre.
        """
        skills = db.query(Skill).filter(Skill.project_id == project_id).all()
        return SkillService.build_skill_tree(skills)

    @staticmethod
    def build_skill_tree(skills: list) -> list:
        """
        Construit un arbre de compétences à partir d'une liste de compétences.
        """
        skill_map = {skill.id: skill for skill in skills}
        root_skills = []

        for skill in skills:
            if skill.parent_id:
                parent = skill_map.get(skill.parent_id)
                if parent:
                    parent.children.append(skill)
            else:
                root_skills.append(skill)

        return root_skills

    @staticmethod
    def unlock_skill(db: Session, skill_id: int) -> Skill:
        """
        Débloque une compétence et permet de passer à ses enfants.
        """
        skill = db.query(Skill).filter(Skill.id == skill_id).first()
        if not skill:
            raise ValueError("Skill not found.")

        skill.is_unlocked = True
        db.commit()
        db.refresh(skill)
        return skill
