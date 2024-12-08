from pydantic import BaseModel


class CreateSessionRequest(BaseModel):
    priceId: str
    token: str


class WebhookEvent(BaseModel):
    id: str
    type: str
    data: dict
