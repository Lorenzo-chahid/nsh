from sqlalchemy.orm import Session
from app.db.models import (
    UserCourseProgress,
    Course,
    SubGoal,
    UserSectionProgress,
)
from app.services.project_analyzer import ProjectAnalyzer
from app.services.course_service import CourseService


def complete_course(user_id: int, course_id: int, db: Session, openai_api_key: str):
    # Marquer le cours comme terminé pour l'utilisateur
    course_progress = (
        db.query(UserCourseProgress)
        .filter(
            UserCourseProgress.user_id == user_id,
            UserCourseProgress.course_id == course_id,
        )
        .first()
    )
    course_progress.is_completed = True
    db.commit()

    # Marquer le sous-objectif associé comme terminé
    course = db.query(Course).filter(Course.id == course_id).first()
    sub_goal = db.query(SubGoal).filter(SubGoal.id == course.subgoal_id).first()
    sub_goal.is_completed = True
    db.commit()

    # Débloquer le prochain sous-objectif
    next_sub_goal = (
        db.query(SubGoal)
        .filter(
            SubGoal.project_id == course.project_id,
            SubGoal.is_unlocked == False,
            SubGoal.is_completed == False,
        )
        .order_by(SubGoal.id)
        .first()
    )

    if next_sub_goal:
        next_sub_goal.is_unlocked = True
        db.commit()

        # Générer le cours pour le nouveau sous-objectif débloqué
        course_service = CourseService(openai_api_key)
        course_service.generate_course_from_subgoal(
            next_sub_goal, db, course.project_id
        )
    else:
        print("Tous les sous-objectifs ont été complétés.")
