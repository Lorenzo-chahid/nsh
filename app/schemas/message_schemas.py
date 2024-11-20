# app/schemas/message_schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MessageBase(BaseModel):
    user_id: int
    user_name: str
    message: str
    page: str
    is_admin: Optional[bool] = False


class CreateMessage(MessageBase):
    pass


class Message(MessageBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
