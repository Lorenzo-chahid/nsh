from sqlalchemy.orm import Session
from app.db.models import IAState


class IAService:
    def __init__(self, ia_state: IAState):
        self.ia_state = ia_state

    def gain_experience(self, exp: int):
        self.ia_state.experience += exp
        self.check_level_up()

    def check_level_up(self):
        # Calcul du seuil d'XP en fonction du niveau actuel
        level_threshold = self.calculate_level_threshold(self.ia_state.level)

        # Monter de niveau si suffisamment d'XP est accumulée
        while self.ia_state.experience >= level_threshold and self.ia_state.level < 25:
            self.ia_state.level += 1
            self.ia_state.skill_points += 1
            self.ia_state.experience -= level_threshold  # Soustraire le seuil d'XP
            level_threshold = self.calculate_level_threshold(
                self.ia_state.level
            )  # Recalculer pour le niveau suivant

    def calculate_level_threshold(self, level: int) -> int:
        """
        Cette fonction retourne le seuil d'XP nécessaire pour monter au niveau suivant.
        La progression devient de plus en plus lente après le niveau 10.
        """
        if level < 5:
            return 100  # Niveau 0 à 5 : 100 XP
        elif level < 10:
            return 200  # Niveau 5 à 10 : 200 XP
        elif level < 15:
            return 500  # Niveau 10 à 15 : 500 XP
        elif level < 21:
            return 1000  # Niveau 15 à 21 : 1000 XP
        else:
            return 2000  # Niveau 21 à 25 : 2000 XP

    def allocate_skill_point(self, skill: str):
        if self.ia_state.skill_points > 0:
            self.ia_state.skills[skill] += 1
            self.ia_state.skill_points -= 1
        else:
            raise ValueError("Pas assez de points de compétence.")
