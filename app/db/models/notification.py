# app/db/models/notification.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.models import Base
from datetime import datetime
import enum


class NotificationType(enum.Enum):
    EVENT_INVITE = "event_invite"
    EVENT_RESPONSE = "event_response"
    EVENT_MODIFICATION = "event_modification"
    OTHER = "other"


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    target_id = Column(Integer, nullable=True)
    target_type = Column(
        Enum(NotificationType), default=NotificationType.OTHER, nullable=False
    )
    message = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relations
    user = relationship("User", foreign_keys=[user_id], back_populates="notifications")
    sender = relationship(
        "User", foreign_keys=[sender_id], back_populates="sent_notifications"
    )
