# app/schemas/course_schemas.py

from pydantic import BaseModel
from typing import List, Optional
from app.schemas.section_schemas import SectionResponse


# Schéma pour la création d'un cours
class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int  # ID du projet auquel ce cours est associé


# Schéma pour la réponse après la création ou la récupération d'un cours
class CourseResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    order: Optional[int]
    sections: Optional[List[SectionResponse]] = []

    class Config:
        from_attributes = True  # Pour la compatibilité avec les modèles ORM
