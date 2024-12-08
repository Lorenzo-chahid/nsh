from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.dependencies import get_current_user
from app.schemas.ai_schemas import AIRequest, AIResponse
from app.services.ai_service import AIService
import logging

router = APIRouter()


@router.post("/generate_course", response_model=AIResponse)
async def generate_course(
    request: AIRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Interagit avec l'IA pour aider l'utilisateur à créer un cours.
    """
    try:
        # Appel au service AI pour obtenir une réponse
        ai_response = await AIService.generate_course_content(request, current_user)

        # Enregistrer le cours généré en base de données si nécessaire
        # Vous pouvez appeler une fonction de service pour cela

        return AIResponse(content=ai_response)
    except Exception as e:
        logging.error(f"Erreur lors de la génération du cours : {str(e)}")
        raise HTTPException(
            status_code=400, detail="Erreur lors de la génération du cours."
        )
