from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User, Project
from app.services.form_service import FormService
from app.schemas.form_schemas import (
    WeightLossForm,
    LanguageLearningForm,
    ProjectResponse,
)
from app.api.v1.dependencies import get_current_user
import os  # Import pour accéder aux variables d'environnement

router = APIRouter()


@router.post("/weight-loss/", response_model=ProjectResponse)
def submit_weight_loss_form(
    form_data: WeightLossForm,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        if not current_user or not current_user.id:
            raise HTTPException(status_code=401, detail="Utilisateur non authentifié")

        # Récupérer la clé API OpenAI depuis les variables d'environnement
        openai_api_key = os.getenv("OPENAI_API_KEY", default=None)
        if not openai_api_key:
            raise HTTPException(
                status_code=500,
                detail="Clé API OpenAI non trouvée dans les variables d'environnement",
            )

        project = FormService.create_weight_loss_form(
            db, form_data, current_user.id, openai_api_key
        )

        return project  # Retourne directement le dictionnaire sans encapsulation
    except Exception as e:
        print("Erreur lors de la soumission :", str(e))
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/weight-loss", response_model=ProjectResponse)
def get_weight_loss_plan(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    # Recherchez le projet de perte de poids pour l'utilisateur actuel
    project = (
        db.query(Project)
        .filter(
            Project.user_id == current_user.id,
            Project.category == "health",
            Project.name == "Programme de Perte de Poids",
        )
        .first()
    )
    print("heeere :: ", project)
    if not project:
        raise HTTPException(status_code=404, detail="Plan introuvable")

    # Retourne les détails du projet avec le programme généré
    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "duration": project.duration,
        "category": project.category,
        "created_at": project.created_at,
        "user_id": project.user_id,
        "program": project.generated_plan,  # Utilise generated_plan
    }


@router.post("/language-learning/", response_model=ProjectResponse)
def submit_language_learning_form(
    form_data: LanguageLearningForm,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        if not current_user or not current_user.id:
            raise HTTPException(status_code=401, detail="Utilisateur non authentifié")

        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise HTTPException(
                status_code=500,
                detail="Clé API OpenAI non trouvée dans les variables d'environnement",
            )

        project = FormService.create_language_learning_course(
            db, form_data, current_user.id, openai_api_key
        )

        return project  # Retourne directement le projet avec le cours généré
    except Exception as e:
        print("Erreur lors de la soumission :", str(e))
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/language-learning/{project_id}", response_model=ProjectResponse)
def get_language_learning_course(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Recherchez le projet de cours de langue pour l'utilisateur actuel
    project = (
        db.query(Project)
        .filter(Project.user_id == current_user.id, Project.id == project_id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Cours introuvable")

    # Retourne les détails du projet avec le cours généré
    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "duration": project.duration,
        "category": project.category,
        "created_at": project.created_at,
        "user_id": project.user_id,
        "program": project.generated_plan,  # Utilise generated_plan
    }
