from fastapi_mail import FastMail, MessageSchema
from typing import List
from app.config.email_config import conf


async def send_email(
    subject: str, recipients: List[str], body: str, subtype: str = "html"
):
    """
    Envoie un email à un ou plusieurs destinataires.

    :param subject: Sujet de l'email
    :param recipients: Liste des adresses email des destinataires
    :param body: Corps du message (HTML ou texte brut)
    :param subtype: Type de contenu (html ou plain)
    """
    message = MessageSchema(
        subject=subject,
        recipients=recipients,  # Liste des destinataires
        body=body,
        subtype=subtype,
    )

    fm = FastMail(conf)
    await fm.send_message(message)
