# tests/test_auth.py

import pytest
from tests.utils import generate_unique_email


def test_signup(client):
    email = generate_unique_email()
    response = client.post(
        "/api/v1/signup",
        json={"email": email, "username": "testuser2", "password": "password2"},
    )
    assert response.status_code == 200


def test_login(client):
    email = generate_unique_email()
    client.post(
        "/api/v1/signup",
        json={"email": email, "username": "testlogin", "password": "password"},
    )

    response = client.post(
        "/api/v1/login",
        json={"email": email, "password": "password"},
    )
    assert response.status_code == 200
