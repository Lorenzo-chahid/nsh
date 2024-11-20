# app/core/settings_prod.py

import os
from dotenv import load_dotenv

load_dotenv()  # Charger les variables d'environnement

class ProdSettings:
    # Configuration de PostgreSQL pour la production sur Render.com
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@host:port/dbname")

    SECRET_KEY = os.getenv("SECRET_KEY", "prodsecretkey")
    DEBUG = False
    ENV = "production"
