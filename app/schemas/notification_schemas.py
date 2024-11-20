# app/schemas/notification_schemas.py

import enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NotificationType(enum.Enum):
    EVENT_INVITE = "event_invite"
    EVENT_RESPONSE = "event_response"
    EVENT_MODIFICATION = "event_modification"  # Nouveau type ajouté
    OTHER = "other"


class NotificationBase(BaseModel):
    message: str
    is_read: bool = False
    target_id: Optional[int] = None
    target_type: NotificationType


class NotificationCreate(NotificationBase):
    user_id: int
    sender_id: Optional[int] = None


class RespondToInvitationRequest(BaseModel):
    response: str


class NotificationResponse(BaseModel):
    id: int
    user_id: int
    sender_id: Optional[int]
    target_id: Optional[int]
    target_type: str  # Remplacez Enum par str pour la sortie
    message: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True

        @staticmethod
        def schema_extra(schema: dict, model: type):
            # Ajoutez un mapping pour rendre le `target_type` lisible
            if "properties" in schema:
                schema["properties"]["target_type"] = {
                    "type": "string",
                    "description": "Le type de notification",
                    "enum": [
                        "event_invite",
                        "event_response",
                        "event_modification",
                        "other",
                    ],
                }
