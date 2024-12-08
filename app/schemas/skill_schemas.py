from pydantic import BaseModel
from typing import List, Optional, Dict


class SkillBase(BaseModel):
    name: str
    description: str
    order: int
    is_unlocked: bool = False
    parent_id: Optional[int] = None


class SkillCreate(SkillBase):
    project_id: int


class SkillResponse(SkillBase):
    id: int
    children: List["SkillResponse"] = []  # Les sous-compétences

    class Config:
        from_attributes = True


class GenerateSkillsRequest(BaseModel):
    """
    Représente les données nécessaires pour générer les compétences.
    """

    project_id: int
    user_data: Dict[str, str]  # Données utilisateur (input du formulaire)


class GenerateSkillsResponse(BaseModel):
    """
    Représente la réponse contenant les compétences générées.
    """

    skills: List[SkillResponse]
