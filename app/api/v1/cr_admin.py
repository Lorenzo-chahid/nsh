import bcrypt
from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine, Base
from app.db.models import Admin

Base.metadata.create_all(bind=engine)


def create_admin(username: str, password: str, is_super_admin=False):
    # Hacher le mot de passe
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )

    # Créer une session DB
    db = SessionLocal()
    admin = Admin(
        username=username,
        hashed_password=hashed_password,
        is_super_admin=is_super_admin,
        permissions=(
            {"manage_users": True, "manage_content": True} if is_super_admin else {}
        ),
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)
    db.close()
    print(f"Admin '{username}' created with ID: {admin.id}")


# Exemple d'utilisation
if __name__ == "__main__":
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    is_super_admin = input("Is super admin? (y/n): ").lower() == "y"
    create_admin(username, password, is_super_admin)
