# app/services/user.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.auth import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Créer un nouvel utilisateur
def create_user(db: Session, user_data: UserCreate):
    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(email=user_data.email, username=user_data.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Lire tous les utilisateurs
def get_users(db: Session):
    return db.query(User).all()

# Mettre à jour un utilisateur
def update_user(db: Session, user_id: int, user_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.email = user_data.email
    user.username = user_data.username
    user.hashed_password = pwd_context.hash(user_data.password)
    db.commit()
    db.refresh(user)
    return user

# Supprimer un utilisateur
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted"}
