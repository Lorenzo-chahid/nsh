# app/core/security.py

from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import os

# Récupération de la clé secrète depuis les variables d'environnement
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "your-secret-key"
)  # Remplacez par une clé secrète sécurisée dans vos variables d'environnement
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Temps d'expiration du token d'accès
REFRESH_TOKEN_EXPIRE_DAYS = 7  # Temps d'expiration du token de rafraîchissement

# Contexte pour hasher les mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Fonctions de gestion des mots de passe
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Vérifie si le mot de passe en clair correspond au mot de passe hashé.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash le mot de passe en utilisant bcrypt.
    """
    return pwd_context.hash(password)


# Fonctions de création de token
def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Crée un token JWT d'accès avec une durée de validité.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    """
    Crée un token JWT de rafraîchissement avec une durée de validité plus longue.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Fonctions de vérification des tokens
def verify_token(token: str, token_type: str = "access"):
    """
    Vérifie la validité du token JWT et s'assure qu'il correspond au type spécifié (access ou refresh).
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != token_type:
            raise ValueError("Invalid token type.")
        username: str = payload.get("sub")
        if username is None:
            raise ValueError("Invalid token payload.")
        return payload
    except JWTError as e:
        raise ValueError("Token is invalid or expired.") from e
