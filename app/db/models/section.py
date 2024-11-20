# app/db/models/section.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
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
