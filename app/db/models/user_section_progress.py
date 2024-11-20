# app/db/models/user_section_progress.py

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class UserSectionProgress(Base):
    __tablename__ = "user_section_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    section_id = Column(Integer, ForeignKey("sections.id"))
    is_completed = Column(Boolean, default=False)

    # Relations
    user = relationship("User", back_populates="section_progress")
    section = relationship("Section", back_populates="user_progress")
