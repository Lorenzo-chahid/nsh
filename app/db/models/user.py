from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.models import Base  # Importer Base depuis base.py


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    visited_pages = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    is_premium = Column(Boolean, default=False)
    stripe_customer_id = Column(String, nullable=True)
    stripe_subscription_id = Column(String, nullable=True)
    user_projects = relationship(
        "UserProject", back_populates="user", cascade="all, delete-orphan"
    )
    projects = relationship(
        "Project", back_populates="owner", cascade="all, delete-orphan"
    )

    # Relations
    projects = relationship("Project", back_populates="owner")
    skill_trees = relationship("SkillTree", back_populates="user")
    ia_state = relationship("IAState", back_populates="user", uselist=False)
    user_exercises = relationship("UserExercise", back_populates="user")
    section_progress = relationship("UserSectionProgress", back_populates="user")
    course_progress = relationship("UserCourseProgress", back_populates="user")
    notifications = relationship(
        "Notification",
        foreign_keys="Notification.user_id",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    sent_notifications = relationship(
        "Notification",
        foreign_keys="Notification.sender_id",
        back_populates="sender",
        cascade="all, delete-orphan",
    )

    # Relations pour les événements
    created_events = relationship(
        "Event", back_populates="created_by", cascade="all, delete-orphan"
    )
    event_participants = relationship(
        "EventParticipant", back_populates="user", cascade="all, delete-orphan"
    )
    events = relationship(
        "Event",
        secondary="event_participants",
        back_populates="participants",
        overlaps="event_participants",
    )
