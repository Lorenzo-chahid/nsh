from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User, IAState
from app.services.ia_service import IAService
import openai
import os

router = APIRouter()

# Utiliser la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY", default=None)


class ChatRequest(BaseModel):
    user_id: int
    user_input: str


def categorize_project(user_input: str) -> str:
    """
    Utilise OpenAI pour déterminer la catégorie du projet à partir de l'input utilisateur.
    Retourne une catégorie : 'Finance', 'Santé', 'Éducation', 'Business', 'Autre'.
    """
    prompt = f"Catégorise l'intention suivante dans l'une de ces catégories : 'Finance', 'Santé', 'Éducation', 'Business', 'Autre'. Intention : '{user_input}'"
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo", prompt=prompt, max_tokens=5, temperature=0
        )
        category = response.choices[0].text.strip()
        return category
    except openai.error.OpenAIError as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur lors de la catégorisation : {str(e)}"
        )


@router.post("/chat/")
def chat_with_ia(request: ChatRequest, db: Session = Depends(get_db)):
    # Récupérer l'utilisateur
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # Récupérer ou créer l'état de l'IA
    ia_state = user.ia_state
    if not ia_state:
        # Créer un état d'IA s'il n'existe pas encore
        ia_state = IAState(
            user_id=user.id, level=0, experience=0, skill_points=0, skills={}
        )
        db.add(ia_state)
        db.commit()
        db.refresh(ia_state)  # Rafraîchir pour obtenir l'ID de l'état IA

    ia_service = IAService(ia_state)

    # Si l'IA est au niveau 0, ne faire que la catégorisation
    if ia_state.level == 0:
        category = categorize_project(request.user_input)
        ia_service.gain_experience(10)  # L'utilisateur gagne 10 XP pour l'interaction

        db.commit()

        return {
            "response": f"Votre projet semble être de la catégorie : {category}. Pour plus de fonctionnalités, augmentez votre IA de niveau.",
            "level": ia_state.level,
            "skill_points": ia_state.skill_points,
            "skills": ia_state.skills,
        }

    # Si l'IA est au niveau supérieur à 0, elle peut interagir de manière conversationnelle
    else:
        # Appel à l'API OpenAI pour obtenir la réponse de l'IA
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es une IA personnelle qui aide l'utilisateur.",
                },
                {"role": "user", "content": request.user_input},
            ],
        )

        ia_service.gain_experience(10)  # 10 XP par interaction

        db.commit()

        return {
            "response": response.choices[0].message["content"],
            "level": ia_state.level,
            "skill_points": ia_state.skill_points,
            "skills": ia_state.skills,
        }
