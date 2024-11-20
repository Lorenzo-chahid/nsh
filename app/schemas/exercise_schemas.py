# app/schemas/exercise_schemas.py

from pydantic import BaseModel
from typing import Optional


class ExerciseBase(BaseModel):
    question: str
    answer: str


class ExerciseCreate(ExerciseBase):
    section_id: int
    order: Optional[int] = None  # Ajout du champ 'order' pour la création


class ExerciseResponse(ExerciseBase):
    id: int
    order: Optional[int] = None  # Ajout du champ 'order' pour la réponse

    class Config:
        from_attributes = (
            True  # Assure la compatibilité avec les objets ORM de SQLAlchemy
        )
