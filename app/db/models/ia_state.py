# app/db/models/ia_state.py

from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.models import Base


class IAState(Base):
    __tablename__ = "ia_states"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    skill_points = Column(Integer, default=0)
    total_points = Column(Integer, default=0)
    statistics = Column(JSON, default={})
    skills = Column(
        JSON,
        default={
            "memory": 0,
            "personality": 0,
            "edit_message": 0,
            "conversation_history": 0,
        },
    )

    # Relation
    user = relationship("User", back_populates="ia_state")
