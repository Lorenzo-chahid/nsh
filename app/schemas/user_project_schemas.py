from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserProjectBase(BaseModel):
    user_id: int
    project_id: int


class UserProjectCreate(UserProjectBase):
    pass


class UserProjectResponse(UserProjectBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
