# app/db/models/event_participant.py

from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.models import Base
import enum


class ParticipantStatus(enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"


class EventParticipant(Base):
    __tablename__ = "event_participants"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(
        Enum(ParticipantStatus), default=ParticipantStatus.PENDING, nullable=False
    )

    # Relations
    event = relationship(
        "Event", back_populates="event_participants", overlaps="participants"
    )
    user = relationship("User", back_populates="event_participants", overlaps="events")
