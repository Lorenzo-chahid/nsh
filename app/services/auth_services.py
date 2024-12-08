# app/services/auth.py

from sqlalchemy.orm import Session
from passlib.context import CryptContext
import jwt
from jwt import decode, ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from fastapi import HTTPException
from app.db.models import User
from app.schemas.auth_schemas import UserCreate
import os

# Initialisation de bcrypt pour le hashage des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Variables pour les tokens JWT
SECRET_KEY = os.getenv(
    "SECRET_KEY", "your-secret-key"
)  # Assurez-vous de définir SECRET_KEY dans vos variables d'environnement
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # Ajusté à 15 minutes
REFRESH_TOKEN_EXPIRE_DAYS = 7


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Vérifie si le mot de passe en clair correspond au mot de passe haché.
    """
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user_by_identifier(
    db: Session, identifier: str, password: str
) -> User:
    """
    Authentifie un utilisateur en utilisant soit son email, soit son username.
    """
    user = (
        db.query(User)
        .filter((User.email == identifier) | (User.username == identifier))
        .first()
    )
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_user(db: Session, user_data: UserCreate) -> User:
    """
    Crée un nouvel utilisateur après avoir vérifié l'unicité de l'email et du username.
    """
    print("HOAHOJABGHKA", user_data)
    existing_user = (
        db.query(User)
        .filter((User.email == user_data.email) | (User.username == user_data.username))
        .first()
    )
    if existing_user:
        return None

    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password,
        profile_picture=user_data.profile_picture,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_access_token(data: dict) -> str:
    """
    Crée un token d'accès JWT avec une expiration.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict) -> str:
    """
    Crée un refresh token JWT avec une expiration plus longue.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str, token_type: str = "access") -> dict:
    """
    Vérifie et décode un token JWT.
    """
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def refresh_access_token_service(refresh_token: str, db: Session) -> str:
    """
    Rafraîchit un token d'accès en utilisant un refresh token valide.
    """
    payload = verify_token(refresh_token, token_type="refresh")
    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    new_access_token = create_access_token({"sub": user.email})
    return new_access_token
