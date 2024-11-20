# app/db/models/course.py

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    order = Column(Integer, nullable=True)
    is_completed = Column(Boolean, default=False)
    is_unlocked = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey("projects.id"))
    subgoal_id = Column(Integer, ForeignKey("sub_goals.id"), nullable=True)

    # Relations
    project = relationship("Project", back_populates="courses")
    sections = relationship(
        "Section", back_populates="course", cascade="all, delete-orphan"
    )
    user_progress = relationship("UserCourseProgress", back_populates="course")
    subgoal = relationship("SubGoal", back_populates="course", uselist=False)
