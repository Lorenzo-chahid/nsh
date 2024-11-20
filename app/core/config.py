# app/core/config.py

import os
from app.core.settings_local import LocalSettings
from app.core.settings_prod import ProdSettings

# Sélectionner les paramètres en fonction de l'environnement
ENV = os.getenv("ENV", "local")

if ENV == "production":
    settings = ProdSettings()
else:
    settings = LocalSettings()
