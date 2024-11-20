# app/db/models/skill_tree.py

from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class SkillTree(Base):
    __tablename__ = "skill_trees"

    id = Column(Integer, primary_key=True, index=True)
    skill_name = Column(String, nullable=False)
    progress = Column(Integer, default=0)
    unlocked = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relation
    user = relationship("User", back_populates="skill_trees")
