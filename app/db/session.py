import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.db.models import Base

# Détection de l'environnement
ENV = os.getenv("ENV", "local")  # Par défaut, en local

# Configuration de la base de données
if ENV == "production":
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://nsh_user:oEcyrsakHYk9MJ6vWLhd2wozx2t2BeUI@dpg-csv20om8ii6s73emv3lg-a.frankfurt-postgres.render.com/nsh",
    )
else:
    DATABASE_URL = (
        "sqlite+aiosqlite:///./test.db"  # Utilisation de `aiosqlite` en local
    )

# Configuration du moteur de base de données
if ENV == "production":
    # PostgreSQL en production
    ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    engine = create_engine(DATABASE_URL)  # Synchrone
    async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)  # Asynchrone
else:
    # SQLite en local
    engine = create_engine(
        DATABASE_URL.replace("+aiosqlite", ""),
        connect_args={"check_same_thread": False},  # Synchrone
    )
    async_engine = create_async_engine(DATABASE_URL, echo=True)  # Asynchrone

# Création des factories de session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Sync
async_session = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)  # Async


# Dépendance pour les sessions synchrones
def get_db():
    """
    Gère une session synchrone pour la base de données.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dépendance pour les sessions asynchrones
async def get_async_db():
    """
    Gère une session asynchrone pour la base de données.
    """
    async with async_session() as session:
        yield session
