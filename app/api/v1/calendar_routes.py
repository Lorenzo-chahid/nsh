from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.api.v1.dependencies import get_current_user
from app.db.models import (
    User,
    Event,
    Project,
    Notification,
    EventParticipant,
    ParticipantStatus,
)
from app.schemas.calendar_schemas import EventCreate, EventUpdate, EventResponse
from datetime import timedelta
from app.db.models import (
    NotificationType,
)  # Assurez-vous d'importer NotificationType

router = APIRouter(prefix="/calendar", tags=["Calendar"])


@router.get("/events", response_model=List[EventResponse])
def get_events(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    # Récupérer les événements acceptés
    user_events = (
        db.query(Event)
        .join(Event.participants)
        .filter(EventParticipant.user_id == current_user.id)
        .filter(EventParticipant.status == ParticipantStatus.ACCEPTED)
        .all()
    )

    return [
        EventResponse(
            id=event.id,
            title=event.title,
            description=event.description,
            start=event.start,
            end=event.end,
            is_shared=event.is_shared,
            created_by_id=event.created_by_id,
            participants=[p.user_id for p in event.event_participants],
        )
        for event in user_events
    ]


@router.post("/events", response_model=EventResponse)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if event.start >= event.end:
        raise HTTPException(
            status_code=400, detail="La date de fin doit être après la date de début."
        )

    # Créer l'événement
    new_event = Event(
        title=event.title,
        description=event.description,
        start=event.start,
        end=event.end,
        is_shared=event.is_shared,
        created_by_id=current_user.id,
    )
    db.add(new_event)
    db.flush()

    # Ajouter les participants et créer les notifications
    for user_id in event.participants_ids:
        participant = EventParticipant(
            event_id=new_event.id,
            user_id=user_id,
            status=ParticipantStatus.PENDING,
        )
        db.add(participant)

        notification = Notification(
            user_id=user_id,
            sender_id=current_user.id,
            target_id=new_event.id,
            target_type=NotificationType.EVENT_INVITE,
            message=f"Vous avez été invité à l'événement '{new_event.title}' par {current_user.username}.",
        )
        db.add(notification)

    db.commit()
    db.refresh(new_event)

    # Construire manuellement la réponse pour éviter les problèmes de validation
    return EventResponse(
        id=new_event.id,
        title=new_event.title,
        description=new_event.description,
        start=new_event.start,
        end=new_event.end,
        is_shared=new_event.is_shared,
        created_by_id=new_event.created_by_id,
        participants=[p.user_id for p in new_event.event_participants],
    )


@router.put("/events/{event_id}", response_model=EventResponse)
def update_event(
    event_id: int,
    event_update: EventUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifier si l'événement existe
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    if event.created_by_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Non autorisé à mettre à jour cet événement"
        )

    # Mettre à jour les champs
    event.title = event_update.title
    event.description = event_update.description
    event.start = event_update.start
    event.end = event_update.end
    event.is_shared = event_update.is_shared

    # Mettre à jour les participants
    if event_update.is_shared and event_update.participants_ids:
        participants = (
            db.query(User).filter(User.id.in_(event_update.participants_ids)).all()
        )
        if not participants:
            raise HTTPException(status_code=400, detail="Participants non valides.")
        event.participants = participants
    else:
        event.participants = [current_user]

    db.commit()
    db.refresh(event)

    # Retourner l'événement avec les participants sous forme d'IDs
    return EventResponse(
        id=event.id,
        title=event.title,
        description=event.description,
        start=event.start,
        end=event.end,
        is_shared=event.is_shared,
        created_by_id=event.created_by_id,
        participants=[participant.id for participant in event.participants],
    )


@router.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifier si l'événement existe
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    if event.created_by_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Non autorisé à supprimer cet événement"
        )

    db.delete(event)
    db.commit()
    return {"detail": "Événement supprimé avec succès"}


@router.post("/events/{event_id}/respond")
def respond_to_event_invitation(
    event_id: int,
    response: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Vérifier si l'utilisateur a une invitation pour cet événement
    participant = (
        db.query(EventParticipant)
        .filter_by(event_id=event_id, user_id=current_user.id)
        .first()
    )
    if not participant:
        raise HTTPException(status_code=404, detail="Invitation non trouvée.")

    # Vérifier si la réponse est valide
    if response.lower() not in ["accept", "decline"]:
        raise HTTPException(status_code=400, detail="Réponse invalide.")

    # Mettre à jour le statut
    participant.status = (
        ParticipantStatus.ACCEPTED
        if response.lower() == "accept"
        else ParticipantStatus.DECLINED
    )

    # Notification au créateur de l'événement
    if response.lower() == "accept":
        notification = Notification(
            user_id=participant.event.created_by_id,
            sender_id=current_user.id,
            target_id=event_id,
            target_type=NotificationType.EVENT_RESPONSE,
            message=f"{current_user.username} a accepté l'invitation à l'événement '{participant.event.title}'.",
        )
        db.add(notification)

    db.commit()
    return {
        "detail": f"Invitation {'acceptée' if response.lower() == 'accept' else 'refusée'} avec succès."
    }
