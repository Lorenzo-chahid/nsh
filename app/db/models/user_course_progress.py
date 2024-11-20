# app/db/models/user_course_progress.py

from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class UserCourseProgress(Base):
    __tablename__ = "user_course_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    completion_rate = Column(Float, default=0.0)
    is_completed = Column(Boolean, default=False)

    # Relations
    user = relationship("User", back_populates="course_progress")
    course = relationship("Course", back_populates="user_progress")
