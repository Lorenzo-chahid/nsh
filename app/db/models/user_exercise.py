# app/db/models/user_exercise.py

from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class UserExercise(Base):
    __tablename__ = "user_exercises"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    is_completed = Column(Boolean, default=False)
    user_answer = Column(Text, nullable=True)
    points_earned = Column(Integer, default=0)

    # Relations
    user = relationship("User", back_populates="user_exercises")
    exercise = relationship("Exercise", back_populates="user_exercises")
