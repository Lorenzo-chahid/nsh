# app/schemas/skill_tree_schemas.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SkillBase(BaseModel):
    name: str = Field(..., example="Flask")
    description: Optional[str] = Field(
        None, example="A micro web framework for Python."
    )
    difficulty_level: int = Field(1, example=3)
    project_id: int = Field(..., example=1)


class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Django")
    description: Optional[str] = Field(
        None, example="A high-level Python web framework."
    )
    difficulty_level: Optional[int] = Field(None, example=4)
    project_id: Optional[int] = Field(None, example=1)


class SkillTreeResponse(SkillBase):
    id: int

    class Config:
        from_attributes = True


class SkillResponse(SkillBase):
    id: int

    class Config:
        from_attributes = True


class SkillTreeCreate(SkillBase):
    pass
