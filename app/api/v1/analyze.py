# api/v1/analyze_route.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.analyze_service import categorize_input, AnalyzeResponse

# Créer le routeur FastAPI
router = APIRouter()


# Modèle de la requête de l'utilisateur
class AnalyzeRequest(BaseModel):
    input: str


# Route FastAPI pour analyser l'input de l'utilisateur
@router.post("/analyze/", response_model=AnalyzeResponse)
def analyze_user_input(request: AnalyzeRequest):
    user_input = request.input

    if not user_input:
        raise HTTPException(status_code=400, detail="Input manquant")

    # Appel de la fonction pour catégoriser l'input de l'utilisateur
    result = categorize_input(user_input)
    print("POKEMON ATTRAPER :: ", result)
    return result
