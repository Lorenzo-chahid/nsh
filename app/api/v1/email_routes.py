from fastapi import APIRouter, HTTPException
from app.services.email_service import send_email

router = APIRouter()


@router.post("/send-test-email")
async def send_test_email(email: str):
    """
    Envoie un email de test.
    """
    try:
        subject = "Test Email from Nanshe"
        body = """
        <h1>Bienvenue sur Nanshe</h1>
        <p>Ceci est un email de test envoyé depuis l'application Nanshe.</p>
        """
        await send_email(subject, [email], body)
        return {"message": f"Test email sent to {email}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
