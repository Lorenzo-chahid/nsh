# app/services/skill_tree.py

from sqlalchemy.orm import Session
from app.db.models import SkillTree
from app.schemas.skill_tree_schemas import SkillTreeCreate


# Service pour ajouter une compétence
def create_skill(db: Session, skill_data: SkillTreeCreate):
    new_skill = SkillTree(
        skill_name=skill_data.skill_name,
        user_id=skill_data.user_id,
        progress=skill_data.progress,
        unlocked=skill_data.unlocked,
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


# Service pour obtenir toutes les compétences
def get_skills(db: Session):
    return db.query(SkillTree).all()
