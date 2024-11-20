# tests/test_users.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup():
    response = client.post(
        "/api/v1/signup",
        json={"email": "uniqueuser6@example.com", "username": "uniqueuser6", "password": "password123"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_user():
    response = client.post(
        "/api/v1/signup",
        json={"email": "uniqueuser4@example.com", "username": "uniqueuser4", "password": "password123"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_users():
    # Créer un utilisateur pour le test
    signup_response = client.post(
        "/api/v1/signup",
        json={"email": "uniqueuser5@example.com", "username": "uniqueuser5", "password": "password123"},
    )
    assert signup_response.status_code == 200
    token = signup_response.json()["access_token"]

    # Vérifier que l'utilisateur peut être récupéré
    response = client.get(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert len(response.json()) > 0
