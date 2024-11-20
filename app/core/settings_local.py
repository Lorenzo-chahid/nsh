# app/core/settings_local.py

import os
from dotenv import load_dotenv

load_dotenv()  # Charger les variables d'environnement du fichier .env (si nécessaire)

class LocalSettings:
    # Configuration de MySQL pour le développement local
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DB = os.getenv("MYSQL_DB", "nanshe_local")

    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
    DEBUG = True
    ENV = "development"
