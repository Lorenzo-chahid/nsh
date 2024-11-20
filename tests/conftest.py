# tests/conftest.py

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.db.models import Base
from app.db.session import get_db
from fastapi.testclient import TestClient
from app.main import app

# Utiliser SQLite en mémoire pour les tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# Création de l'engine et de la session pour la base de données en mémoire
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Fixture pour réinitialiser la base de données avant chaque test
@pytest.fixture(scope="function")
def db_session():
    # Crée les tables avant chaque test
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Supprime les tables après chaque test
        Base.metadata.drop_all(bind=engine)


# Fixture pour l'API client de FastAPI
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


# Fixture pour nettoyer la base de données
@pytest.fixture(scope="function", autouse=True)
def clean_database(db_session):
    # Nettoyer les tables avant chaque test
    db_session.execute(text("DELETE FROM users"))
    db_session.commit()
