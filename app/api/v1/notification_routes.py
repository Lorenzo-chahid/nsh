from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.db.models import (
    Notification,
    EventParticipant,
    ParticipantStatus,
    User,
    NotificationType,
)
from app.schemas.notification_schemas import (
    NotificationCreate,
    NotificationResponse,
    RespondToInvitationRequest,
)
from app.api.v1.dependencies import get_current_user

router = APIRouter(tags=["Notifications"])


@router.get("/", response_model=List[NotificationResponse])
def get_notifications(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    print(f"Fetching notifications for user: {current_user.id}")  # Log utilisateur
    notifications = (
        db.query(Notification)
        .filter(Notification.user_id == current_user.id)
        .order_by(Notification.created_at.desc())
        .all()
    )

    # Conversion explicite des Enum en chaînes
    response = [
        NotificationResponse(
            id=n.id,
            user_id=n.user_id,
            sender_id=n.sender_id,
            target_id=n.target_id,
            target_type=n.target_type.value,  # Utilisez `.value` pour extraire la chaîne
            message=n.message,
            is_read=n.is_read,
            created_at=n.created_at,
        )
        for n in notifications
    ]
    print(f"Found notifications: {response}")  # Log des notifications
    return response


@router.post("/", response_model=NotificationResponse)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_notification = Notification(
        user_id=notification.user_id,
        sender_id=notification.sender_id,
        target_id=notification.target_id,
        target_type=notification.target_type,
        message=notification.message,
    )
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification


@router.put("/{notification_id}/read")
def mark_notification_as_read(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    notification = (
        db.query(Notification)
        .filter(
            Notification.id == notification_id, Notification.user_id == current_user.id
        )
        .first()
    )
    if not notification:
        raise HTTPException(status_code=404, detail="Notification non trouvée")

    notification.is_read = True
    db.commit()
    return {"detail": "Notification marquée comme lue"}


@router.post("/{notification_id}/respond")
def respond_to_invitation(
    notification_id: int,
    request: RespondToInvitationRequest,  # Utilisation du modèle Pydantic
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    notification = (
        db.query(Notification)
        .filter(
            Notification.id == notification_id,
            Notification.user_id == current_user.id,
        )
        .first()
    )

    if not notification:
        raise HTTPException(status_code=404, detail="Notification non trouvée")

    if request.response.lower() not in ["accept", "decline"]:
        raise HTTPException(status_code=400, detail="Réponse invalide")

    event_participant = (
        db.query(EventParticipant)
        .filter(EventParticipant.event_id == notification.target_id)
        .first()
    )
    if not event_participant:
        raise HTTPException(status_code=404, detail="Événement non trouvé")

    # Mettre à jour le statut de l'invitation
    if request.response.lower() == "accept":
        event_participant.status = ParticipantStatus.ACCEPTED
    elif request.response.lower() == "decline":
        event_participant.status = ParticipantStatus.DECLINED

    # Marquer la notification d'invitation comme lue
    notification.is_read = True

    # Créer une nouvelle notification pour le créateur de l'invitation
    sender_id = notification.sender_id
    response_message = (
        f"{current_user.username} a {request.response.lower()}é votre invitation "
        f"pour l'événement '{notification.message}'."
    )
    new_notification = Notification(
        user_id=sender_id,  # Envoyer au créateur de l'invitation
        sender_id=current_user.id,  # L'utilisateur actuel (répondant)
        target_id=notification.target_id,
        target_type=NotificationType.EVENT_RESPONSE,  # Utilisez l'énumération ici
        message=response_message,
    )

    db.add(new_notification)
    db.commit()

    return {"detail": f"Invitation {request.response}ée avec succès"}


@router.put("/mark-all-read")
def mark_all_notifications_as_read(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    notifications = (
        db.query(Notification)
        .filter(Notification.user_id == current_user.id, Notification.is_read == False)
        .all()
    )
    for notification in notifications:
        notification.is_read = True

    db.commit()
    return {"detail": f"{len(notifications)} notifications marquées comme lues"}
