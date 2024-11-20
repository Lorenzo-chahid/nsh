# app/services/form_service.py

import os
import openai
import re
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.db.models import Project, Course, Section, Event, Exercise
from app.schemas.form_schemas import WeightLossForm, LanguageLearningForm
import json
import random


class FormService:
    @staticmethod
    def create_weight_loss_form(
        db: Session, form_data: WeightLossForm, user_id: int, openai_api_key: str
    ):
        custom_inputs = form_data.dict()
        openai.api_key = openai_api_key
        print("step 1")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Tu es un coach de perte de poids expérimenté et certifié. "
                        "Crée un programme d'accompagnement structuré, précis, détaillé et personnalisé "
                        "à suivre au quotidien ou hebdomadairement pour un utilisateur. "
                        "Assure-toi que chaque conseil est pratique, réalisable et adapté au profil de l'utilisateur."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Je pèse {custom_inputs['current_weight']} kg et souhaite atteindre {custom_inputs['goal_weight']} kg "
                        f"en {custom_inputs['duration']} jours. Mon niveau d'exercice est {custom_inputs['exercise_level']}. "
                        "Peux-tu créer un programme quotidien ou hebdomadaire détaillé que je pourrais suivre directement dans l'application ? "
                        "Inclue des conseils nutritionnels précis, des plans d'exercices adaptés et des recommandations pour le bien-être général."
                    ),
                },
            ],
        )
        print("step 2")
        generated_plan = response["choices"][0]["message"]["content"]
        print(generated_plan)

        # Enregistrement du projet et du plan dans la base de données
        new_project = Project(
            name="Programme de Perte de Poids",
            description="Programme personnalisé de perte de poids",
            duration=form_data.duration,
            category="health",
            user_id=user_id,
            custom_inputs=custom_inputs,
            generated_plan=generated_plan,  # Sauvegarde du plan généré
        )
        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        # Création de l'événement
        start_date = datetime.now()
        end_date = start_date + timedelta(days=new_project.duration)

        new_event = Event(
            title=new_project.name,
            description=new_project.description,
            start=start_date,
            end=end_date,
            is_shared=False,
            created_by_id=user_id,
        )
        db.add(new_event)
        db.commit()

        # Charger les exercices depuis le fichier JSON
        exercises = FormService.load_exercises()

        # Calcul du nombre total de semaines
        total_weeks = new_project.duration // 7
        if new_project.duration % 7 != 0:
            total_weeks += 1

        # Mappez le niveau de l'utilisateur avec la difficulté des exercices
        user_level = custom_inputs["exercise_level"]  # 'low', 'moderate', 'high'
        level_mapping = {
            "low": ["Beginner"],
            "moderate": ["Beginner", "Intermediate"],
            "high": ["Intermediate", "Advanced"],
        }

        available_exercises = [
            ex for ex in exercises if ex["difficulty"] in level_mapping[user_level]
        ]

        for week_number in range(1, total_weeks + 1):
            week_course = Course(
                title=f"Semaine {week_number}",
                description=f"Programme pour la semaine {week_number}",
                project_id=new_project.id,
                is_unlocked=(
                    True if week_number == 1 else False
                ),  # Débloque la première semaine
            )
            db.add(week_course)
            db.commit()
            db.refresh(week_course)

            # Créer les sections pour chaque jour de la semaine
            for day_number in range(1, 8):
                # Vérifier si nous n'avons pas dépassé la durée totale
                if (week_number - 1) * 7 + day_number > new_project.duration:
                    break

                # Sélectionner un exercice en fonction du niveau
                exercise = random.choice(available_exercises)

                day_section = Section(
                    title=f"Jour {day_number}",
                    content=(
                        f"Exercice du jour : {exercise['name']}\n\n"
                        f"Description : {exercise['description']}\n\n"
                        f"Muscles travaillés : {', '.join(exercise['muscle_groups'])}"
                    ),
                    course_id=week_course.id,
                )
                db.add(day_section)
                db.commit()
                db.refresh(day_section)

                # Créer un quiz pour le jour
                quiz = Exercise(
                    question=f"Combien de calories brûle en moyenne l'exercice {exercise['name']} par heure ?",
                    answer=str(exercise["average_calories_per_hour"]),
                    section_id=day_section.id,
                )
                db.add(quiz)
                db.commit()

        # Retourne les détails du projet avec le programme structuré
        return {
            "id": new_project.id,
            "name": new_project.name,
            "description": new_project.description,
            "duration": new_project.duration,
            "category": new_project.category,
            "created_at": new_project.created_at,
            "user_id": new_project.user_id,
            "program": generated_plan,  # Programme structuré
        }

    @staticmethod
    def load_exercises():
        # Assurez-vous que le fichier 'exercises.json' est dans le bon répertoire
        with open("exercises.json", "r", encoding="utf-8") as f:
            exercises = json.load(f)
        return exercises

    # ... Autres méthodes (create_language_learning_course, etc.) ...

    @staticmethod
    def extract_week_content(plan_text: str, week_title: str) -> str:
        # Utilise les expressions régulières pour extraire le contenu d'une semaine spécifique
        pattern = rf"{week_title}.*?(?=####|\Z)"
        match = re.search(pattern, plan_text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(0).strip()
        else:
            return ""

    @staticmethod
    def create_language_learning_course(
        db: Session, form_data: LanguageLearningForm, user_id: int, openai_api_key: str
    ):
        custom_inputs = form_data.dict()
        language = custom_inputs["language"]
        current_level = custom_inputs["current_level"]
        learning_method = custom_inputs["learning_method"]
        duration = custom_inputs["duration"]

        # Définir la clé API OpenAI
        openai.api_key = openai_api_key

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"Tu es un professeur de {language} expérimenté. "
                        f"Crée un programme d'apprentissage structuré, précis et détaillé pour un élève de niveau {current_level}. "
                        "Le programme doit couvrir l'alphabet, les bases de grammaire, le vocabulaire essentiel et des exercices pratiques. "
                        "Le cours doit être en français."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Je souhaite apprendre {language} en partant de zéro. "
                        f"Ma méthode d'apprentissage préférée est {learning_method}, et je prévois d'étudier pendant {duration} mois. "
                        "Peux-tu créer un programme détaillé pour moi ?"
                    ),
                },
            ],
        )

        generated_course = response["choices"][0]["message"]["content"]

        # Enregistrement du projet et du cours dans la base de données
        new_project = Project(
            name=f"Apprentissage de {language}",
            description=f"Programme personnalisé pour apprendre {language}",
            duration=duration,
            category="language_learning",
            user_id=user_id,
            custom_inputs=custom_inputs,
            generated_plan=generated_course,  # Sauvegarde du cours généré
        )
        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        # Retourne les détails du projet avec le cours structuré
        return {
            "id": new_project.id,
            "name": new_project.name,
            "description": new_project.description,
            "duration": new_project.duration,
            "category": new_project.category,
            "created_at": new_project.created_at,
            "user_id": new_project.user_id,
            "program": generated_course,  # Cours structuré
        }
