from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.models import Base  # Importer Base depuis base.py


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    is_shared = Column(Boolean, default=False)
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relations
    created_by = relationship("User", back_populates="created_events")
    event_participants = relationship(
        "EventParticipant", back_populates="event", cascade="all, delete-orphan"
    )
    participants = relationship(
        "User",
        secondary="event_participants",
        back_populates="events",
        overlaps="event_participants",
    )
