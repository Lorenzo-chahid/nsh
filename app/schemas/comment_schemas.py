# app/schemas/comment_schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CommentBase(BaseModel):
    content: str
    project_id: int


class CommentCreate(CommentBase):
    pass


class CommentUpdate(BaseModel):
    content: Optional[str] = None
    project_id: Optional[int] = None


class CommentResponse(CommentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
