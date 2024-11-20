# app/schemas/project_schemas.py

from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    duration: int
    category: str
    is_public: bool = True
    custom_inputs: Optional[Dict] = None
    is_generated_by_platform: bool = False
    generated_plan: Optional[str] = None


class ProjectCreate(ProjectBase):
    user_id: int


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    category: Optional[str] = None
    is_public: Optional[bool] = None
    custom_inputs: Optional[Dict] = None
    is_generated_by_platform: Optional[bool] = None
    generated_plan: Optional[str] = None


class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
