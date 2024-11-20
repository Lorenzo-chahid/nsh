# app/api/v1/skill_tree.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.skill_tree_schemas import SkillTreeCreate, SkillTreeResponse
from app.services.skill_tree import create_skill, get_skills
from app.db.session import get_db

router = APIRouter()


# Route pour ajouter une compétence à l'arbre
@router.post("/", response_model=SkillTreeResponse)
def create_skill_entry(skill: SkillTreeCreate, db: Session = Depends(get_db)):
    return create_skill(db, skill)


# Route pour obtenir la liste des compétences
@router.get("/", response_model=list[SkillTreeResponse])
def list_skills(db: Session = Depends(get_db)):
    return get_skills(db)
