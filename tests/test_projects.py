# tests/test_projects.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_project():
    # Créer un utilisateur pour le test
    signup_response = client.post(
        "/api/v1/signup",
        json={
            "email": "projectuser@example.com",
            "username": "projectuser",
            "password": "password123",
        },
    )
    assert signup_response.status_code == 200
    token = signup_response.json()["access_token"]

    # Utiliser le token pour créer un projet
    project_data = {
        "name": "Test Project",
        "description": "This is a test project description.",
        "duration": 30,
        "category": "Education",
    }
    response = client.post(
        "/api/v1/projects/",
        json=project_data,
        headers={"Authorization": f"Bearer {token}"},
    )

    # Vérifier que la création du projet a réussi
    assert response.status_code == 200, f"Project creation failed: {response.text}"
    response_data = response.json()
    assert response_data["name"] == project_data["name"]
    assert response_data["description"] == project_data["description"]
    assert response_data["duration"] == project_data["duration"]
    assert response_data["category"] == project_data["category"]

    # Vérifier que le projet est bien associé à l'utilisateur
    assert response_data["user_id"] is not None
