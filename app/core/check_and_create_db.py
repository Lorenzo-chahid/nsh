# app/db/check_and_create_db.py (pour MySQL)

import pymysql
from config import settings

def create_mysql_db_if_not_exists():
    # Connexion sans spécifier de base de données pour la créer si nécessaire
    connection = pymysql.connect(
        host=settings.MYSQL_HOST,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            # Vérifier si la base de données existe
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.MYSQL_DB}")
            print(f"Database '{settings.MYSQL_DB}' verified/created successfully.")
    finally:
        connection.close()

if __name__ == "__main__":
    create_mysql_db_if_not_exists()
