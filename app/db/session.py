# app/db/session.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.db.models import Base  # Import Base from models

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Synchronous engine
if "sqlite" in DATABASE_URL:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

# Asynchronous engine
ASYNC_DATABASE_URL = DATABASE_URL.replace("sqlite://", "sqlite+aiosqlite://")
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)

# Synchronous session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Asynchronous session
async_session = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


# Dependency for synchronous sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency for asynchronous sessions
async def get_async_db():
    async with async_session() as session:
        yield session
