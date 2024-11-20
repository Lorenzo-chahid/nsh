# app/schemas/auth.py

from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: str
    username: str
    password: str

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserLogin(BaseModel):
    identifier: str  # email ou username
    password: str

    @classmethod
    def model_validate(cls, **kwargs):
        print("Validating data:", kwargs)  # Log les données reçues
        return super().model_validate(**kwargs)
