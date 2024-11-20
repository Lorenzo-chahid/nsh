from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.auth import UserCreate, UserResponse
from app.services.user import create_user, get_users, delete_user, update_user
from app.db.session import get_db

router = APIRouter()


# Lire tous les utilisateurs
@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [
        UserResponse.model_validate(user) for user in users
    ]  # Utiliser from_orm pour la conversion


# Créer un nouvel utilisateur
@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


# Mettre à jour un utilisateur
@router.put("/{user_id}", response_model=UserResponse)
def update_user_info(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)


# Supprimer un utilisateur
@router.delete("/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
