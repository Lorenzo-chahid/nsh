from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.future import select
from app.schemas.project_schemas import ProjectCreate, ProjectResponse
from app.schemas.user_project_schemas import UserProjectResponse
from app.db.session import get_db
from app.api.v1.dependencies import get_current_user
from app.db.models import User, Project, SubGoal, Course, Section, UserProject
from app.services.project_analyzer import ProjectAnalyzer
from sqlalchemy.dialects import postgresql

import os

router = APIRouter()


@router.post("/", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    print("Creating new project with user:", current_user)
    try:
        # Récupérer la clé API OpenAI depuis les variables d'environnement
        openai_api_key = os.getenv("OPENAI_API_KEY", default=None)
        if not openai_api_key:
            raise HTTPException(
                status_code=500,
                detail="Clé API OpenAI non trouvée dans les variables d'environnement",
            )

        # Créer le projet sans le commettre pour obtenir un project_id
        new_project = Project(
            name=project.name,
            description=project.description,
            duration=project.duration,
            category=project.category,
            user_id=current_user.id,
        )
        db.add(new_project)
        db.flush()  # Assigne un ID à new_project sans commettre
        db.refresh(new_project)

        # Étape 1 : Utiliser ProjectAnalyzer pour classer l'intention
        analyzer = ProjectAnalyzer(openai_api_key)
        category = analyzer.classify_input(project.description)
        new_project.category = category  # Mettre à jour la catégorie du projet

        print("Catégorie identifiée :", category)

        # Étape 2 : Utiliser l'analyseur de projet pour analyser la description
        analysis = analyzer.analyze_project(
            project_description=project.description,
            db=db,
            project_id=new_project.id,
            is_premium=current_user.is_premium,
        )

        # Enregistrer le plan généré dans le projet
        new_project.generated_plan = analysis.get("generated_plan", "")

        # Enregistrer les sous-objectifs et autres détails si nécessaire
        # Vous pouvez ajouter du code ici pour traiter 'analysis' et mettre à jour 'new_project' ou d'autres modèles

        # Log les détails de l'analyse pour vérifier qu'ils sont valides
        print("Analysis results:", analysis)

        # Maintenant, on peut commettre les changements
        db.commit()

        return new_project
    except Exception as e:
        print("Error while creating project:", str(e))
        db.rollback()  # Annule les changements non commis en cas d'erreur
        raise HTTPException(
            status_code=400, detail=f"Project creation failed: {str(e)}"
        )


@router.get("/public", response_model=List[ProjectResponse])
def get_public_projects(db: Session = Depends(get_db)):
    public_projects = db.query(Project).filter(Project.is_public == True).all()
    return public_projects


@router.get("/", response_model=List[ProjectResponse])
async def list_user_projects(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = db.execute(
        select(Project)
        .options(
            selectinload(Project.courses)
            .selectinload(Course.sections)
            .selectinload(Section.exercises)
        )
        .where((Project.user_id == current_user.id))
    )
    user_projects = result.scalars().all()
    return user_projects


@router.get("/", response_model=list[ProjectResponse])
def list_projects(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    print("khbskjbj")
    projects = db.query(Project).filter(Project.user_id == current_user.id).all()
    for project in projects:
        print(
            f"Project ID: {project.id}, Name: {project.name}, Category: {project.category}"
        )
        print(f"Generated Plan: {project}...")  # Affiche les 100 premiers caractères
        courses = project.courses
        if courses:
            for course in courses:
                print(
                    f"  Course ID: {course.id}, Title: {course.title}, Description: {course.description}"
                )
        else:
            print("  No courses found for this project.")
    return projects


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project_by_id(
    project_id: int,
    db: AsyncSession = Depends(get_db),
):
    print("PIUKACHU")
    # Supprimer le filtre sur user_id
    result = db.execute(
        select(Project)
        .options(
            selectinload(Project.courses)
            .selectinload(Course.sections)
            .selectinload(Section.exercises)
        )
        .where(Project.id == project_id)
    )

    project = result.scalars().first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Log des détails du projet
    print(f"Project ID: {project.id}")
    print(f"Name: {project.name}")
    print(f"Description: {project.description}")
    print(f"Duration: {project.duration}")
    print(f"Category: {project.category}")
    print(f"Created At: {project.created_at}")

    # Log des cours liés au projet
    if project.courses:
        print("Courses:")
        for course in project.courses:
            print(f"  Course ID: {course.id}")
            print(f"  Title: {course.title}")
            print(f"  Description: {course.description}")
            if course.sections:
                print("  Sections:")
                for section in course.sections:
                    print(f"    Section ID: {section.id}")
                    print(f"    Title: {section.title}")
                    print(f"    Content: {section.content}")
                    if section.exercises:
                        print("    Exercises:")
                        for exercise in section.exercises:
                            print(f"      Exercise ID: {exercise.id}")
                            print(f"      Question: {exercise.question}")
                            print(f"      Answer: {exercise.answer}")
    else:
        print("No courses found.")

    return project


@router.get("/subgoals/{project_id}")
def get_project_sub_goals(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifier que le projet appartient à l'utilisateur actuel
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == current_user.id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404, detail="Project not found or access denied."
        )

    # Récupérer les sous-objectifs associés au projet
    sub_goals = db.query(SubGoal).filter(SubGoal.project_id == project_id).all()

    # Préparer les sous-objectifs pour la réponse JSON
    sub_goals_data = [
        {
            "id": sub_goal.id,
            "title": sub_goal.title,
            "description": sub_goal.description,
            "prerequisites": sub_goal.prerequisites,
        }
        for sub_goal in sub_goals
    ]

    return {"sub_goals": sub_goals_data}


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifier que le projet appartient à l'utilisateur actuel
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == current_user.id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404, detail="Project not found or access denied."
        )

    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}


@router.post("/{project_id}/sub_goals/{sub_goal_id}/complete")
def complete_sub_goal(
    project_id: int,
    sub_goal_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Vérifier que le projet appartient à l'utilisateur actuel
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == current_user.id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404, detail="Project not found or access denied."
        )

    # Récupérer le sous-objectif
    sub_goal = (
        db.query(SubGoal)
        .filter(SubGoal.id == sub_goal_id, SubGoal.project_id == project_id)
        .first()
    )

    if not sub_goal:
        raise HTTPException(status_code=404, detail="Sub-goal not found")

    # Marquer le sous-objectif comme terminé
    sub_goal.is_completed = True
    db.commit()

    # Déverrouiller le sous-objectif suivant
    next_sub_goal = (
        db.query(SubGoal)
        .filter(
            SubGoal.project_id == project_id,
            SubGoal.is_completed == False,
            SubGoal.is_unlocked == False,
        )
        .first()
    )
    if next_sub_goal:
        next_sub_goal.is_unlocked = True
        db.commit()

    return {"message": "Sub-goal completed and next sub-goal unlocked"}


@router.get("/subgoal/{sub_goal_id}")
def get_sub_goal_by_id(
    sub_goal_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    sub_goal = db.query(SubGoal).filter(SubGoal.id == sub_goal_id).first()

    if not sub_goal:
        raise HTTPException(status_code=404, detail="Sub-goal not found")

    return {
        "id": sub_goal.id,
        "title": sub_goal.title,
        "description": sub_goal.description,
        "prerequisites": sub_goal.prerequisites,
    }


@router.post("/{project_id}/subscribe", response_model=UserProjectResponse)
async def subscribe_to_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifiez si le projet public existe
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projet introuvable")

    # Vérifiez si l'utilisateur est déjà inscrit
    existing_subscription = db.execute(
        select(UserProject).where(
            UserProject.user_id == current_user.id,
            UserProject.project_id == project_id,
        )
    )
    if existing_subscription.scalars().first():
        raise HTTPException(
            status_code=400, detail="Vous êtes déjà inscrit à ce projet"
        )

    # Créez l'abonnement
    user_project = UserProject(user_id=current_user.id, project_id=project_id)
    db.add(user_project)
    db.commit()
    db.refresh(user_project)

    return user_project


@router.delete("/{project_id}/unsubscribe", response_model=dict)
async def unsubscribe_from_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifiez si l'utilisateur est inscrit à ce projet
    user_project = await db.execute(
        select(UserProject).where(
            UserProject.user_id == current_user.id,
            UserProject.project_id == project_id,
        )
    )
    user_project = user_project.scalars().first()
    if not user_project:
        raise HTTPException(
            status_code=404, detail="Vous n'êtes pas inscrit à ce projet"
        )

    # Supprimez l'abonnement
    await db.delete(user_project)
    await db.commit()

    return {"detail": "Projet supprimé de vos projets"}
