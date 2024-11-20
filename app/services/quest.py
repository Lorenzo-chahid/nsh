# app/services/quest.py

from sqlalchemy.orm import Session
from app.db.models import Quest
from app.schemas.quest_schemas import QuestCreate


# Service pour créer une nouvelle quête
def create_quest(db: Session, quest_data: QuestCreate):
    new_quest = Quest(
        title=quest_data.title,
        description=quest_data.description,
        project_id=quest_data.project_id,
    )
    db.add(new_quest)
    db.commit()
    db.refresh(new_quest)
    return new_quest


# Service pour obtenir toutes les quêtes
def get_quests(db: Session):
    return db.query(Quest).all()
