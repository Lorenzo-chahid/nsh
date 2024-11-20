# app/schemas/admin_schemas.py

from pydantic import BaseModel


class AdminLogin(BaseModel):
    username: str
    password: str


class AdminResponse(BaseModel):
    access_token: str
    token_type: str
