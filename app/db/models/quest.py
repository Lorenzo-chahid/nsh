# app/db/models/quest.py

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False)
    progress = Column(Integer, default=0)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Relation
    project = relationship("Project", back_populates="quests")
