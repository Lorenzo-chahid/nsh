# app/main.py

from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketDisconnect,
    Depends,
    HTTPException,
    status,
)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.data.ukrainian_course_data import courses_data

from app.db.session import (
    async_engine,
    async_session,
    get_async_db,
)  # Import depuis session.py
from app.db.models import Base  # Import Base depuis models
from app.schemas.message_schemas import Message, CreateMessage
from app.schemas.notification_schemas import NotificationResponse
from app.api.v1.notification_routes import router as notifications_router
from app.db.models import (
    messages,
    Notification,
    User,
    Admin,
    EventParticipant,
    ParticipantStatus,
    Exercise,
    Project,  # Importé correctement
    Course,  # Importé correctement
    Skill,  # Importé correctement
    Section,
)
from app.api.v1 import (
    auth,
    projects,
    quests,
    skill_tree,
    courses,
    users,
    chatbot,
    analyze,
    forms,
    admin as admin_routes,  # Renommé pour éviter le conflit avec le module admin
)
from app.api.v1.calendar_routes import router as calendar_router
from typing import List
import asyncio
import json
import jwt
import logging
from app.core.security import hash_password, verify_token  # Import depuis security.py

# Configuration de l'application FastAPI
app = FastAPI()

# Configuration CORS
origins = [
    "*",
    "http://localhost:3000",  # Adresse de votre frontend React
    "*",  # Autoriser toutes les origines (à ajuster pour la production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration JWT
SECRET_KEY = "VOTRE_SECRET_KEY"  # Remplacez par votre clé secrète
ALGORITHM = "HS256"


# Gestionnaire de connexions WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print("Nouvelle connexion WebSocket acceptée.")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        print("Connexion WebSocket déconnectée.")

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)
        print(f"Message diffusé à {len(self.active_connections)} connexions.")


manager = ConnectionManager()


# Fonction pour créer le projet public
# Dans app/main.py


async def create_project_from_file(course_data_file):
    """
    Génère un projet public, ses cours, sections, exercices et compétences à partir d'un fichier de données.

    :param course_data_file: Module contenant les données du projet à importer.
    """
    # Importation dynamique du fichier de données
    data = __import__(
        course_data_file,
        fromlist=["courses_data", "project_name", "project_description"],
    )

    async with async_session() as db:
        try:
            # Vérifier si le projet existe déjà
            project_name = getattr(data, "project_name", "Unnamed Project")
            project_description = getattr(
                data, "project_description", "No description provided."
            )
            courses_data = getattr(data, "courses_data", [])

            result = await db.execute(
                select(Project).where(Project.name == project_name)
            )
            existing_project = result.scalars().first()
            if existing_project:
                logging.info(f"Le projet '{project_name}' existe déjà.")
                return

            # Créer le projet
            project = Project(
                name=project_name,
                description=project_description,
                duration=len(courses_data)
                * 10,  # Exemple : durée basée sur le nombre de cours
                category="Langue",
                is_public=True,
                is_generated_by_platform=True,
                user_id=None,  # Projet généré par la plateforme
            )
            db.add(project)
            await db.commit()
            await db.refresh(project)
            logging.info(f"Projet '{project_name}' créé avec l'ID {project.id}")

            # Créer les cours, sections et exercices
            for course_data in courses_data:
                course = Course(
                    title=course_data["title"],
                    description=course_data["description"],
                    order=course_data.get("order"),
                    project_id=project.id,
                )
                db.add(course)
                await db.commit()
                await db.refresh(course)
                logging.info(f"Cours '{course.title}' créé avec l'ID {course.id}")

                # Créer les sections du cours
                for section_data in course_data.get("sections", []):
                    section = Section(
                        title=section_data["title"],
                        content=section_data["content"],
                        order=section_data.get("order"),
                        course_id=course.id,
                    )
                    db.add(section)
                    await db.commit()
                    await db.refresh(section)
                    logging.info(
                        f"Section '{section.title}' créée avec l'ID {section.id}"
                    )

                    # Créer les exercices de la section
                    for exercise_data in section_data.get("exercises", []):
                        exercise = Exercise(
                            question=exercise_data["question"],
                            answer=exercise_data["answer"],
                            order=exercise_data.get("order"),
                            section_id=section.id,
                        )
                        db.add(exercise)
                        await db.commit()
                        await db.refresh(exercise)
                        logging.info(
                            f"Exercice '{exercise.question}' créé avec l'ID {exercise.id}"
                        )

            # Créer les compétences associées au projet
            skills_data = getattr(data, "skills_data", [])
            for skill_data in skills_data:
                skill = Skill(
                    name=skill_data["name"],
                    description=skill_data["description"],
                    difficulty_level=skill_data["difficulty_level"],
                    project_id=project.id,
                )
                db.add(skill)
                await db.commit()
                await db.refresh(skill)
                logging.info(f"Compétence '{skill.name}' créée avec l'ID {skill.id}")

            logging.info(
                f"Le projet public '{project_name}' avec ses cours, sections, exercices et compétences associés a été créé."
            )
        except Exception as e:
            logging.error(
                f"Une erreur est survenue lors de la création du projet public: {e}"
            )
            await db.rollback()
        finally:
            await db.close()


# Reste de votre code (endpoints REST, WebSockets, etc.)


# Initialisation des tables et création des utilisateurs à la création
@app.on_event("startup")
async def on_startup():
    # Importer tous les modèles pour les enregistrer avec Base
    from app.db import models

    # Créer toutes les tables
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Toutes les tables ont été créées.")

    # Créer les utilisateurs de test et l'administrateur
    async with async_session() as db:
        # Définir les utilisateurs à créer
        initial_users = [
            {"username": "test1", "email": "test1@example.com", "password": "password"},
            {"username": "test2", "email": "test2@example.com", "password": "password"},
        ]

        # Créer les utilisateurs de test
        for user_data in initial_users:
            stmt = select(User).where(User.username == user_data["username"])
            result = await db.execute(stmt)
            user = result.scalars().first()
            if not user:
                try:
                    new_user = User(
                        username=user_data["username"],
                        email=user_data["email"],
                        hashed_password=hash_password(
                            user_data["password"]
                        ),  # Utilisation de security.py
                        is_active=True,
                        is_premium=False,
                    )
                    db.add(new_user)
                    await db.commit()
                    print(f"Utilisateur {user_data['username']} créé avec succès.")
                except Exception as e:
                    await db.rollback()
                    print(
                        f"Erreur lors de la création de l'utilisateur {user_data['username']}: {e}"
                    )

        # Créer l'utilisateur administrateur
        admin_username = "admin"
        admin_email = "admin@example.com"
        admin_password = "password"

        stmt = select(Admin).where(Admin.username == admin_username)
        result = await db.execute(stmt)
        admin = result.scalars().first()
        if not admin:
            try:
                new_admin = Admin(
                    username=admin_username,
                    email=admin_email,
                    hashed_password=hash_password(
                        admin_password
                    ),  # Utilisation de security.py
                    is_super_admin=True,
                    permissions={
                        "all": True
                    },  # Définissez les permissions selon vos besoins
                    contact_email="admin_contact@example.com",
                    phone_number="1234567890",
                    profile_details="Administrateur du système.",
                )
                db.add(new_admin)
                await db.commit()
                print("Administrateur créé avec succès.")
            except Exception as e:
                await db.rollback()
                print(f"Erreur lors de la création de l'administrateur: {e}")

    # Appeler la fonction pour créer le projet public
    await create_project_from_file("app.data.ukrainian_course_data")


# Inclure les routes existantes
app.include_router(auth.router, prefix="/api/v1", tags=["Auth"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["Projects"])
app.include_router(quests.router, prefix="/api/v1", tags=["Quests"])
app.include_router(skill_tree.router, prefix="/api/v1", tags=["Skill Tree"])
app.include_router(courses.router, prefix="/api/v1", tags=["Courses"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["Chatbot"])
app.include_router(analyze.router, prefix="/api/v1", tags=["Analyze"])
app.include_router(forms.router, prefix="/api/v1/forms", tags=["Forms"])
app.include_router(admin_routes.router, prefix="/api/v1/admin", tags=["Admin"])
app.include_router(
    notifications_router, prefix="/api/v1/notifications", tags=["Notifications"]
)
app.include_router(
    calendar_router, prefix="/api/v1", dependencies=[Depends(get_async_db)]
)


# Exemple de route de test
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Nanshe!"}
