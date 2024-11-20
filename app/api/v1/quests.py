# app/api/v1/quests.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.quest_schemas import QuestCreate, QuestResponse
from app.services.quest import create_quest, get_quests
from app.db.session import get_db

router = APIRouter()


# Route pour créer une nouvelle quête
@router.post("/", response_model=QuestResponse)
def create_new_quest(quest: QuestCreate, db: Session = Depends(get_db)):
    return create_quest(db, quest)


# Route pour obtenir la liste des quêtes
@router.get("/", response_model=list[QuestResponse])
def list_quests(db: Session = Depends(get_db)):
    return get_quests(db)
