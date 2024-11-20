# app/api/v1/auth.py

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.schemas.auth import UserCreate, Token, UserLogin
from app.services.auth import (
    create_user,
    authenticate_user_by_identifier,
    create_access_token,
    create_refresh_token,
    verify_token,
    refresh_access_token_service,
)
from app.db.session import get_db
from app.db.models import User
import logging

router = APIRouter()

# Configurer le logging
logging.basicConfig(level=logging.DEBUG)

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


# Endpoint pour inscrire un utilisateur
@router.post("/signup", response_model=Token)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Créer des tokens pour l'utilisateur nouvellement inscrit
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    logging.debug(f"Nouvel utilisateur créé: {user.email}")

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


# Endpoint pour connecter un utilisateur avec email ou username
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        logging.debug(f"Payload reçu : {user.dict()}")
        authenticated_user = authenticate_user_by_identifier(
            db, user.identifier, user.password
        )
        if not authenticated_user:
            logging.debug("Utilisateur non authentifié.")
            raise HTTPException(
                status_code=400, detail="Incorrect identifier or password"
            )

        access_token = create_access_token({"sub": authenticated_user.email})
        refresh_token = create_refresh_token({"sub": authenticated_user.email})

        logging.debug(f"Tokens générés pour l'utilisateur: {authenticated_user.email}")

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
    except HTTPException as he:
        logging.error(f"HTTPException: {he.detail}")
        raise he
    except Exception as e:
        logging.exception("Erreur pendant le login")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Endpoint pour rafraîchir le token d'accès
@router.post("/refresh-token", response_model=Token)
def refresh_access_token(refresh_token: str = Body(...), db: Session = Depends(get_db)):
    try:
        new_access_token = refresh_access_token_service(refresh_token, db)
        logging.debug(f"Nouveau token d'accès généré pour le refresh token.")
        return {
            "access_token": new_access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
    except HTTPException as he:
        logging.error(f"HTTPException lors du rafraîchissement du token: {he.detail}")
        raise he
    except Exception as e:
        logging.exception("Erreur lors du rafraîchissement du token")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Route protégée avec JWT
@router.get("/protected-route")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {"message": "This is a protected route"}


# Fonction pour obtenir l'utilisateur à partir du token
@router.get("/me")
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = verify_token(token)
    email = payload.get("sub")
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
