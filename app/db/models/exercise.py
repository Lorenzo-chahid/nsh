# app/db/models/exercise.py

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


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
