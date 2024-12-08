from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User
from app.core.security import verify_token
from app.schemas.payment_schemas import CreateSessionRequest
import stripe

router = APIRouter()

# Configurez Stripe avec votre clé secrète
stripe.api_key = "sk_test_51QO6NIDc4Et5GayXDGi2XkSsASc3VnrO3GsOg6g67WhuYHT3tuqSOQCUOCclX6y4t8JlneTTCFblDXbtJvcYMycP00tQaj8frg"

WEBHOOK_SECRET = (
    "whsec_dabc1efba7961ea62cc3de94807ff7745eef7a356a6fea970da08b21d3b603a8"
)


def get_current_user(token: str, db: Session):
    """
    Récupère l'utilisateur actuel à partir du token JWT.
    """
    payload = verify_token(token)
    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


@router.post("/create-session")
def create_payment_session(
    request: CreateSessionRequest,
    db: Session = Depends(get_db),
):
    """
    Crée une session Stripe Checkout et lie l'utilisateur connecté.
    """
    print("Received request:", request)

    user = get_current_user(request.token, db)
    print("Authenticated user:", user.email)

    # Si l'utilisateur n'a pas de customer ID Stripe, en créer un
    if not user.stripe_customer_id:
        print("Difgimon 8338")
        customer = stripe.Customer.create(
            email=user.email,
            name=f"{user.first_name or ''} {user.last_name or ''}".strip(),
        )
        user.stripe_customer_id = customer.id
        db.commit()

    try:
        session = stripe.checkout.Session.create(
            customer=user.stripe_customer_id,
            payment_method_types=["card"],
            line_items=[
                {
                    "price": request.priceId,
                    "quantity": 1,
                }
            ],
            mode="subscription",
            success_url="https://localhost:8000.com/success",
            cancel_url="https://localhost:8000.com/cancel",
        )
        return {"sessionId": session.id}
    except Exception as e:
        print("Stripe error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    """
    Écoute les webhooks Stripe pour mettre à jour l'utilisateur après un paiement réussi.
    """
    payload = await request.body()
    sig_header = request.headers.get("Stripe-Signature")

    try:
        # Validez le payload reçu avec la signature et la clé secrète
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
        print("Stripe Event Received:", event)

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Gestion des événements Stripe
    if event["type"] == "checkout.session.completed":
        session_data = event["data"]["object"]
        customer_id = session_data.get("customer")

        # Récupérer l'utilisateur associé dans la base de données
        user = db.query(User).filter(User.stripe_customer_id == customer_id).first()
        if user:
            user.stripe_subscription_id = session_data.get("subscription")
            user.is_premium = True
            db.commit()
            print(f"User {user.email} upgraded to premium.")

    return {"status": "success"}
