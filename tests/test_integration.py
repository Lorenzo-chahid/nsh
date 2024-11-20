# tests/test_integration.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_full_integration():
    response = client.post(
        "/api/v1/signup",
        json={"email": "integrationuser@example.com", "username": "integrationuser", "password": "password123"},
    )
    assert response.status_code == 200  # Vérifie que l'inscription s'est bien passée