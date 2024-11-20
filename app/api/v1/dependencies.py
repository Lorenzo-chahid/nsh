from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session
from app.db.models import User
from app.db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    print("Token received:", token)  # Print pour vérifier le token reçu
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        print("Payload decoded:", payload)  # Print pour voir le payload du token
        if user_email is None:
            print("User email not found in token payload")
            raise credentials_exception
    except JWTError as e:
        print("JWT Error:", e)  # Print pour voir l'erreur JWT
        raise credentials_exception

    user = db.query(User).filter(User.email == user_email).first()
    print("User found:", user)  # Print pour voir l'utilisateur trouvé en DB
    if user is None:
        print("User not found in database")
        raise credentials_exception

    return user
