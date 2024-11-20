# tests/utils.py

import uuid


def generate_unique_email():
    return f"user_{uuid.uuid4()}@example.com"
