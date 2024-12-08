from pydantic import BaseModel
from typing import List, Optional


class AIRequest(BaseModel):
    prompt: str  # Le message de l'utilisateur


class AIResponse(BaseModel):
    content: str  # La réponse de l'IA
