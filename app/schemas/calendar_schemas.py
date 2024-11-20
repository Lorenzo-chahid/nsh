from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


# Base pour les événements
class EventBase(BaseModel):
    title: str = Field(..., example="Réunion de Projet")
    description: Optional[str] = Field(
        None, example="Discussion sur les objectifs du projet."
    )
    start: datetime = Field(..., example="2024-12-01T10:00:00")
    end: datetime = Field(..., example="2024-12-01T11:00:00")
    is_shared: bool = Field(False, example=True)


# Modèle pour créer un événement
class EventCreate(EventBase):
    participants_ids: Optional[List[int]] = Field(default_factory=list, example=[1, 2])


# Modèle pour mettre à jour un événement
class EventUpdate(EventBase):
    participants_ids: Optional[List[int]] = Field(default_factory=list, example=[1, 2])


# Modèle pour la réponse d'un événement
class EventResponse(EventBase):
    id: int
    created_by_id: int
    participants: List[int] = Field(default_factory=list, example=[1, 2])

    class Config:
        from_attributes = True


# Modèle principal de l'événement
class Event(EventBase):
    id: int
    created_by_id: int
    participants: List[int] = Field(default_factory=list, example=[1, 2])

    class Config:
        from_attributes = True
