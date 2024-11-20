# scripts/create_default_admin.py

import os
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Admin
from app.core.security import get_password_hash


def create_default_admin():
    db: Session = SessionLocal()

    # Vérifier si un admin existe déjà avec le nom d'utilisateur 'modeuil'
    existing_admin = db.query(Admin).filter(Admin.username == "modeuil").first()
    if existing_admin:
        print(
            "Un administrateur par défaut avec le nom d'utilisateur 'modeuil' existe déjà."
        )
        db.close()
        return

    # Créer l'administrateur par défaut
    default_admin = Admin(
        username="modeuil",
        hashed_password=get_password_hash("password1234"),
        is_super_admin=True,
        permissions={"all": True},  # Exemple de permissions
    )

    db.add(default_admin)
    db.commit()
    db.close()
    print("Administrateur par défaut créé avec succès :")
    print("Nom d'utilisateur : modeuil")
    print("Mot de passe : password1234")


if __name__ == "__main__":
    create_default_admin()
