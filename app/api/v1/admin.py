# app/api/v1/admin.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import inspect, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Dict, List
from app.db.session import get_db
from app.schemas.admin_schemas import AdminLogin, AdminResponse
from app.schemas.user_schemas import UserCreate, UserUpdate, UserResponse
from app.schemas.project_schemas import ProjectCreate, ProjectUpdate, ProjectResponse
from app.schemas.calendar_schemas import EventCreate, EventUpdate, EventResponse
from app.schemas.comment_schemas import CommentCreate, CommentUpdate, CommentResponse
from app.schemas.quest_schemas import QuestCreate, QuestUpdate, QuestResponse
from app.schemas.skill_tree_schemas import SkillCreate, SkillUpdate, SkillResponse
from app.schemas.ia_schemas import IAStateCreate, IAStateUpdate, IAStateResponse
from app.db.models import Admin, User, Project, Event, Comment, Quest, Skill, IAState
from app.core.security import verify_password, create_access_token, get_password_hash
from app.api.dependencies import get_current_admin
from datetime import timedelta

router = APIRouter(tags=["admin"])


# Route de login admin
@router.post("/login", response_model=AdminResponse)
def admin_login(admin_credentials: AdminLogin, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.username == admin_credentials.username).first()
    if not admin or not verify_password(
        admin_credentials.password, admin.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nom d'utilisateur ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": admin.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


# Routes CRUD pour User


@router.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email déjà enregistré")
    hashed_password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        is_active=user.is_active,
        is_premium=user.is_premium,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=List[UserResponse])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    for var, value in vars(user).items():
        if value is not None:
            setattr(db_user, var, value)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    db.delete(user)
    db.commit()
    return


# Routes CRUD pour Project


@router.post("/projects", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    new_project = Project(
        name=project.name,
        description=project.description,
        duration=project.duration,
        category=project.category,
        is_public=project.is_public,
        custom_inputs=project.custom_inputs,
        is_generated_by_platform=project.is_generated_by_platform,
        generated_plan=project.generated_plan,
        user_id=project.user_id,
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@router.get("/projects", response_model=List[ProjectResponse])
def read_projects(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    projects = db.query(Project).offset(skip).limit(limit).all()
    return projects


@router.get("/projects/{project_id}", response_model=ProjectResponse)
def read_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    return project


@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    for var, value in vars(project).items():
        if value is not None:
            setattr(db_project, var, value)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    db.delete(project)
    db.commit()
    return


# Routes CRUD pour Event


@router.post("/events", response_model=EventResponse)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    new_event = Event(
        title=event.title,
        description=event.description,
        start=event.start,
        end=event.end,
        is_shared=event.is_shared,
        created_by_id=event.created_by_id,
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@router.get("/events", response_model=List[EventResponse])
def read_events(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events


@router.get("/events/{event_id}", response_model=EventResponse)
def read_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    return event


@router.put("/events/{event_id}", response_model=EventResponse)
def update_event(
    event_id: int,
    event: EventUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    for var, value in vars(event).items():
        if value is not None:
            setattr(db_event, var, value)
    db.commit()
    db.refresh(db_event)
    return db_event


@router.delete("/events/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    db.delete(event)
    db.commit()
    return


# Routes CRUD pour Comment


@router.post("/comments", response_model=CommentResponse)
def create_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    new_comment = Comment(content=comment.content, project_id=comment.project_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@router.get("/comments", response_model=List[CommentResponse])
def read_comments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    comments = db.query(Comment).offset(skip).limit(limit).all()
    return comments


@router.get("/comments/{comment_id}", response_model=CommentResponse)
def read_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="Commentaire non trouvé")
    return comment


@router.put("/comments/{comment_id}", response_model=CommentResponse)
def update_comment(
    comment_id: int,
    comment: CommentUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Commentaire non trouvé")
    for var, value in vars(comment).items():
        if value is not None:
            setattr(db_comment, var, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="Commentaire non trouvé")
    db.delete(comment)
    db.commit()
    return


# Routes CRUD pour Quest


@router.post("/quests", response_model=QuestResponse)
def create_quest(
    quest: QuestCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    new_quest = Quest(
        title=quest.title,
        description=quest.description,
        is_completed=quest.is_completed,
        progress=quest.progress,
        project_id=quest.project_id,
    )
    db.add(new_quest)
    db.commit()
    db.refresh(new_quest)
    return new_quest


@router.get("/quests", response_model=List[QuestResponse])
def read_quests(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    quests = db.query(Quest).offset(skip).limit(limit).all()
    return quests


@router.get("/quests/{quest_id}", response_model=QuestResponse)
def read_quest(
    quest_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if quest is None:
        raise HTTPException(status_code=404, detail="Quête non trouvée")
    return quest


@router.put("/quests/{quest_id}", response_model=QuestResponse)
def update_quest(
    quest_id: int,
    quest: QuestUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quête non trouvée")
    for var, value in vars(quest).items():
        if value is not None:
            setattr(db_quest, var, value)
    db.commit()
    db.refresh(db_quest)
    return db_quest


@router.delete("/quests/{quest_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quest(
    quest_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if quest is None:
        raise HTTPException(status_code=404, detail="Quête non trouvée")
    db.delete(quest)
    db.commit()
    return


# Routes CRUD pour Skill


@router.post("/skills", response_model=SkillResponse)
def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    new_skill = Skill(
        name=skill.name,
        description=skill.description,
        difficulty_level=skill.difficulty_level,
        project_id=skill.project_id,
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


@router.get("/skills", response_model=List[SkillResponse])
def read_skills(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    skills = db.query(Skill).offset(skip).limit(limit).all()
    return skills


@router.get("/skills/{skill_id}", response_model=SkillResponse)
def read_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if skill is None:
        raise HTTPException(status_code=404, detail="Compétence non trouvée")
    return skill


@router.put("/skills/{skill_id}", response_model=SkillResponse)
def update_skill(
    skill_id: int,
    skill: SkillUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Compétence non trouvée")
    for var, value in vars(skill).items():
        if value is not None:
            setattr(db_skill, var, value)
    db.commit()
    db.refresh(db_skill)
    return db_skill


@router.delete("/skills/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if skill is None:
        raise HTTPException(status_code=404, detail="Compétence non trouvée")
    db.delete(skill)
    db.commit()
    return


# Routes CRUD pour IAState


@router.post("/ia_states", response_model=IAStateResponse)
def create_ia_state(
    ia_state: IAStateCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    new_ia_state = IAState(
        user_id=ia_state.user_id,
        level=ia_state.level,
        experience=ia_state.experience,
        skill_points=ia_state.skill_points,
        total_points=ia_state.total_points,
        statistics=ia_state.statistics,
        skills=ia_state.skills,
    )
    db.add(new_ia_state)
    db.commit()
    db.refresh(new_ia_state)
    return new_ia_state


@router.get("/ia_states", response_model=List[IAStateResponse])
def read_ia_states(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    ia_states = db.query(IAState).offset(skip).limit(limit).all()
    return ia_states


@router.get("/ia_states/{ia_state_id}", response_model=IAStateResponse)
def read_ia_state(
    ia_state_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    ia_state = db.query(IAState).filter(IAState.id == ia_state_id).first()
    if ia_state is None:
        raise HTTPException(status_code=404, detail="IAState non trouvé")
    return ia_state


@router.put("/ia_states/{ia_state_id}", response_model=IAStateResponse)
def update_ia_state(
    ia_state_id: int,
    ia_state: IAStateUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    db_ia_state = db.query(IAState).filter(IAState.id == ia_state_id).first()
    if db_ia_state is None:
        raise HTTPException(status_code=404, detail="IAState non trouvé")
    for var, value in vars(ia_state).items():
        if value is not None:
            setattr(db_ia_state, var, value)
    db.commit()
    db.refresh(db_ia_state)
    return db_ia_state


@router.delete("/ia_states/{ia_state_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ia_state(
    ia_state_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    ia_state = db.query(IAState).filter(IAState.id == ia_state_id).first()
    if ia_state is None:
        raise HTTPException(status_code=404, detail="IAState non trouvé")
    db.delete(ia_state)
    db.commit()  # Route pour lister toutes les tables et leurs enregistrements


@router.get("/tables", response_model=Dict[str, List[Any]])
def list_all_tables(
    db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)
):
    """
    Liste toutes les tables et leurs enregistrements.
    """
    inspector = inspect(db.bind)
    tables = inspector.get_table_names()
    result = {}

    for table in tables:
        try:
            # Utilisation explicite de `text` pour les requêtes SQL
            records = db.execute(text(f"SELECT * FROM {table}")).fetchall()

            # Convertir les enregistrements en dictionnaires
            # En utilisant `.keys()` si possible ou `.asdict()`
            result[table] = [
                (
                    {column: value for column, value in zip(record.keys(), record)}
                    if hasattr(record, "keys")
                    else dict(record._asdict())
                )
                for record in records
            ]
        except SQLAlchemyError as e:
            # Ajout d'une liste vide pour les tables en erreur
            result[table] = []
            print(
                f"Erreur lors de la récupération des données pour la table {table}: {str(e)}"
            )
        except AttributeError as e:
            # Si la conversion échoue
            result[table] = []
            print(f"Erreur de conversion pour la table {table}: {str(e)}")

    return result


# Vous pouvez continuer à ajouter des routes CRUD pour les autres modèles de la même manière
