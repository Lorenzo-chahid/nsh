# app/schemas/user_schemas.py

from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    username: str
    is_active: bool = True
    is_premium: bool = False
    profile_picture: Optional[str] = None  # URL de l'image de profil


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    is_active: Optional[bool] = None
    is_premium: Optional[bool] = None
    profile_picture: Optional[str]


class UserResponse(UserBase):
    id: int
    created_at: datetime
    last_login: Optional[datetime] = None
    visited_pages: Optional[str] = None
    stripe_customer_id: Optional[str] = None
    profile_picture: Optional[str]
    stripe_subscription_id: Optional[str] = None

    class Config:
        from_attributes = True


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
