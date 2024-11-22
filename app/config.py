import os

# Déterminer l'environnement
ENV = os.getenv("ENV", "development")

# Configuration de la base de données
if ENV == "production":
    # URL pour une base de données PostgreSQL en production
    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://user:password@host:port/dbname"
    )
    ASYNC_DATABASE_URL = DATABASE_URL
else:
    # URL pour SQLite en mode async localement
    DATABASE_URL = "sqlite:///./test.db"
    ASYNC_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
