# app/db/models/project.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    JSON,
    Text,
)
from sqlalchemy.orm import relationship
from app.db.models import Base
from datetime import datetime


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    duration = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    is_public = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    custom_inputs = Column(JSON, nullable=True)
    is_generated_by_platform = Column(Boolean, default=False)
    generated_plan = Column(Text, nullable=True)

    owner = relationship("User", back_populates="projects")
    user_projects = relationship(
        "UserProject", back_populates="project", cascade="all, delete-orphan"
    )
    quests = relationship(
        "Quest", back_populates="project", cascade="all, delete-orphan"
    )
    courses = relationship(
        "Course", back_populates="project", cascade="all, delete-orphan"
    )
    skills = relationship(
        "Skill", back_populates="project", cascade="all, delete-orphan"
    )
    sub_goals = relationship(
        "SubGoal", back_populates="project", cascade="all, delete-orphan"
    )
    comments = relationship(
        "Comment", back_populates="project", cascade="all, delete-orphan"
    )
