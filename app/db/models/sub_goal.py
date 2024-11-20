# app/db/models/sub_goal.py

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class SubGoal(Base):
    __tablename__ = "sub_goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    prerequisites = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False)
    is_unlocked = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Relations
    project = relationship("Project", back_populates="sub_goals")
    course = relationship("Course", back_populates="subgoal", uselist=False)
