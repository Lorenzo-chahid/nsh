# app/schemas/ia_state_schemas.py

from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class IAStateBase(BaseModel):
    user_id: int
    level: int = 1
    experience: int = 0
    skill_points: int = 0
    total_points: int = 0
    statistics: Optional[Dict] = {}
    skills: Optional[Dict] = {
        "memory": 0,
        "personality": 0,
        "edit_message": 0,
        "conversation_history": 0,
    }


class IAStateCreate(IAStateBase):
    pass


class IAStateUpdate(BaseModel):
    user_id: Optional[int] = None
    level: Optional[int] = None
    experience: Optional[int] = None
    skill_points: Optional[int] = None
    total_points: Optional[int] = None
    statistics: Optional[Dict] = None
    skills: Optional[Dict] = None


class IAStateResponse(IAStateBase):
    id: int

    class Config:
        from_attributes = True
