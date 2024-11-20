# app/db/models/skill.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    difficulty_level = Column(Integer, default=1)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Relation
    project = relationship("Project", back_populates="skills")
