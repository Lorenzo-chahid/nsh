from fastapi_mail import ConnectionConfig
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME", "Nanshe"),  # Nom facultatif
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_STARTTLS=True,  # Utilisez STARTTLS pour sécuriser la connexion
    MAIL_SSL_TLS=False,  # Ne pas utiliser SSL/TLS direct
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)
