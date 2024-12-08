from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.skill_schemas import (
    SkillCreate,
    SkillResponse,
    GenerateSkillsRequest,
    GenerateSkillsResponse,
)
from app.services.skill_service import SkillService
from app.db.models import User
from app.api.v1.dependencies import get_current_user
import os
import logging

# Configurez le logging pour tout afficher
logging.basicConfig(level=logging.DEBUG)

router = APIRouter()


@router.post("/generate", response_model=GenerateSkillsResponse)
def generate_skills(
    request: GenerateSkillsRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Génère des compétences pour un projet en utilisant une IA, puis les enregistre.
    """

    import logging

    # Configurez le logging pour tout afficher
    logging.basicConfig(level=logging.DEBUG)
    openai_api_key = "code to find"
    if not openai_api_key:
        logging.error("Clé API OpenAI non configurée.")
        raise HTTPException(status_code=500, detail="Clé API OpenAI non configurée.")

    try:
        # Générer les compétences avec l'IA
        is_premium = current_user.is_premium
        generated_skills = SkillService.generate_skills_with_ai(
            request,
            1,
            "code to find",
        )

        # Enregistrer les compétences générées
        SkillService.save_generated_skills(db, request.project_id, generated_skills)

        logging.info(f"Compétences générées et enregistrées : {generated_skills}")
        return {"skills": generated_skills}
    except Exception as e:
        logging.error(f"Erreur lors de la génération des compétences : {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/project/{project_id}", response_model=SkillResponse)
def get_skills_for_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Récupère toutes les compétences pour un projet spécifique.
    """
    try:
        skills = SkillService.get_skills_for_project(db, project_id)
        return {"skills": skills}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{skill_id}/unlock", response_model=SkillResponse)
def unlock_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Débloque une compétence et permet de progresser dans l'arbre.
    """
    try:
        skill = SkillService.unlock_skill(db, skill_id)
        return skill
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
