# app/schemas/quest_schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class QuestBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    progress: int = 0
    project_id: int


class QuestCreate(QuestBase):
    pass


class QuestUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    progress: Optional[int] = None
    project_id: Optional[int] = None


class QuestResponse(QuestBase):
    id: int

    class Config:
        from_attributes = True
