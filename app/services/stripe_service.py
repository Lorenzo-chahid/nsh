import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_checkout_session(price_id: str, user_email: str):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": price_id,
                    "quantity": 1,
                },
            ],
            mode="subscription",
            success_url="https://your-domain.com/success",
            cancel_url="https://your-domain.com/cancel",
            customer_email=user_email,
        )
        return session
    except Exception as e:
        raise Exception(f"Error creating checkout session: {str(e)}")
