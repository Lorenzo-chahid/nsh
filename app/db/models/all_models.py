# app/db/models/section.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.models import Base


class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    order = Column(Integer, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"))

    # Relations
    course = relationship("Course", back_populates="sections")
    exercises = relationship(
        "Exercise", back_populates="section", cascade="all, delete-orphan"
    )
    user_progress = relationship("UserSectionProgress", back_populates="section")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    order = Column(Integer, nullable=False, default=0)  # L'ordre logique dans l'arbre
    is_unlocked = Column(Boolean, default=False)  # État de déblocage
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    parent_id = Column(
        Integer, ForeignKey("skills.id"), nullable=True
    )  # Compétence parente

    # Relations
    project = relationship("Project", back_populates="skills")
    children = relationship(
        "Skill", back_populates="parent", cascade="all, delete-orphan"
    )
    parent = relationship("Skill", remote_side=[id])

    def __repr__(self):
        return f"<Skill(id={self.id}, name='{self.name}', unlocked={self.is_unlocked})>"


# app/db/models/exercise.py


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    order = Column(Integer, nullable=True)  # Ajout du champ 'order'
    section_id = Column(Integer, ForeignKey("sections.id"))

    # Relations
    section = relationship("Section", back_populates="exercises")
    user_exercises = relationship(
        "UserExercise", back_populates="exercise", cascade="all, delete-orphan"
    )


# app/db/models/course.py


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
