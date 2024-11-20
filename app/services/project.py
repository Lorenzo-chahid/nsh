# services/project.py

from sqlalchemy.orm import Session
from app.db.models import Project, Skill, Quest
from app.schemas.project_schemas import ProjectCreate
from app.services.project_analyzer import ProjectAnalyzer


def create_project(
    db: Session, project_data: ProjectCreate, user_id: int, analyzer: ProjectAnalyzer
):
    # Étape 1 : Analyse du projet avec le ProjectAnalyzer
    analysis_result = analyzer.analyze_project(
        project_description=project_data.description,
        is_premium=False,  # Définir cela dynamiquement si l'utilisateur est premium
    )

    # Étape 2 : Créer le projet
    new_project = Project(
        name=project_data.name,
        description=project_data.description,
        duration=project_data.duration,
        category=project_data.category,
        user_id=user_id,
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    # Étape 3 : Enregistrer les compétences et les sous-objectifs
    for sub_goal in analysis_result.get("sub_goals", []):
        # Enregistrer chaque sous-objectif en tant que "Quest"
        new_quest = Quest(
            title=sub_goal.get("title", "Untitled Quest"),
            description=sub_goal.get("description", ""),
            project_id=new_project.id,
            is_completed=False,
            progress=0,
        )
        db.add(new_quest)

        # Enregistrer les compétences liées à ce sous-objectif
        for skill in sub_goal.get("skills", []):
            new_skill = Skill(
                name=skill["name"],
                description=skill.get("description", ""),
                project_id=new_project.id,
                difficulty_level=skill.get("difficulty_level", 1),
            )
            db.add(new_skill)

    # Étape 4 : Commit pour valider les changements dans la base de données
    db.commit()

    return new_project


def get_projects_for_user(db: Session, user_id: int):
    return db.query(Project).filter(Project.user_id == user_id).all()
