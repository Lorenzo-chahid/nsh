# tests/test_protected_routes.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_protected_route():
    # Créer un utilisateur pour le test
    client.post(
        "/api/v1/signup",
        json={"email": "testprotected@example.com", "username": "testprotected", "password": "password123"},
    )
    
    # Connexion pour obtenir un token JWT
    login_response = client.post(
        "/api/v1/login",
        json={"email": "testprotected@example.com", "password": "password123"},  # Utiliser json au lieu de data
    )
    
    # Vérifier que le login est réussi
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"
    token = login_response.json()["access_token"]
    
    # Utiliser le token pour accéder à la route protégée
    protected_response = client.get(
        "/api/v1/protected-route",
        headers={"Authorization": f"Bearer {token}"},
    )
    
    assert protected_response.status_code == 200
    assert protected_response.json() == {"message": "This is a protected route"}
