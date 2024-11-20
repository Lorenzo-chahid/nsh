# app/db/models/admin.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, Text
from app.db.models import Base
from datetime import datetime


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(
        String, unique=True, index=True, nullable=False
    )  # Ajouté pour l'administrateur
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    is_super_admin = Column(Boolean, default=False)
    permissions = Column(JSON, default={})

    contact_email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    profile_details = Column(Text, nullable=True)

    def has_permission(self, permission: str) -> bool:
        return self.permissions.get(permission, False)
