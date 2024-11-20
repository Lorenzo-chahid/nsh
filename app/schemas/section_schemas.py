# app/schemas/section_schemas.py

from typing import List, Optional
from pydantic import BaseModel
from app.schemas.exercise_schemas import ExerciseResponse


class SectionResponse(BaseModel):
    id: int
    title: str
    content: str
    order: Optional[int]
    exercises: Optional[List[ExerciseResponse]] = []

    class Config:
        from_attributes = True
