# app/db/models/message.py

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    func,
)
from app.db.models import Base

messages = Table(
    "messages",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, ForeignKey("users.id"), index=True),
    Column("user_name", String, index=True),
    Column("message", String, nullable=False),
    Column("timestamp", DateTime(timezone=True), server_default=func.now()),
    Column("page", String, nullable=False),
    Column("is_admin", Boolean, default=False),
)
