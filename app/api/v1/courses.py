from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.dependencies import get_current_user
from app.db.models import Project, Course, Section, Exercise, User, SubGoal
from app.services.course_service import CourseService
import os

router = APIRouter()

# Configuration de l'API Key d'OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", default=None)


@router.get("/courses/user")
def get_user_courses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_projects = db.query(Project).filter(Project.user_id == current_user.id).all()

    if not user_projects:
        raise HTTPException(status_code=404, detail="No projects found for user")

    user_courses = []
    for project in user_projects:
        courses = db.query(Course).filter(Course.project_id == project.id).all()
        user_courses.extend(courses)

    if not user_courses:
        raise HTTPException(status_code=404, detail="No courses found for user")

    return [
        {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "sections": [
                {"title": section.title, "content": section.content}
                for section in course.sections
            ],
        }
        for course in user_courses
    ]


@router.get("/courses")
def get_all_courses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    projects = db.query(Project).filter(Project.user_id == current_user.id).all()

    if not projects:
        raise HTTPException(status_code=404, detail="No projects found")

    courses = (
        db.query(Course)
        .filter(Course.project_id.in_([project.id for project in projects]))
        .all()
    )

    if not courses:
        raise HTTPException(status_code=404, detail="No courses found")

    return [
        {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "sections": [
                {"title": section.title, "content": section.content}
                for section in course.sections
            ],
        }
        for course in courses
    ]


@router.get("/courses/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    project = db.query(Project).filter(Project.id == course.project_id).first()

    if not project or project.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to view this course"
        )

    sections = db.query(Section).filter(Section.course_id == course.id).all()
    exercises = (
        db.query(Exercise)
        .filter(Exercise.section_id.in_([section.id for section in sections]))
        .all()
    )

    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "sections": [
            {"title": section.title, "content": section.content} for section in sections
        ],
        "exercises": [
            {"question": exercise.question, "answer": exercise.answer}
            for exercise in exercises
        ],
    }


def generate_course_from_subgoal(self, subgoal, db: Session, project_id: int):
    try:
        course = Course(
            title=subgoal["title"],
            description=subgoal["description"],
            project_id=project_id,
        )
        db.add(course)
        db.commit()
        db.refresh(course)
        print(f"Course created: {course.title}, ID: {course.id}")

        for skill in subgoal.get("skills", []):
            try:
                section_content = self.generate_lesson_content(skill["name"])
                section = Section(
                    title=f"Learning {skill['name']}",
                    content=section_content,
                    course_id=course.id,
                )
                db.add(section)
                db.commit()
                print(f"Section created: {section.title} for course {course.title}")

                exercise_question, exercise_answer = self.generate_exercise(
                    skill["name"]
                )
                exercise = Exercise(
                    question=exercise_question,
                    answer=exercise_answer,
                    section_id=section.id,
                )
                db.add(exercise)
                print(
                    f"Exercise created for section {section.title}: {exercise_question}"
                )

            except Exception as e:
                print(
                    f"Error creating section or exercise for skill {skill['name']}: {e}"
                )
                db.rollback()

        db.commit()

    except Exception as e:
        print(f"Error generating course for subgoal {subgoal['title']}: {e}")
        db.rollback()


@router.get("/subgoal/{sub_goal_id}/course")
def get_course_by_sub_goal(
    sub_goal_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    sub_goal = db.query(SubGoal).filter(SubGoal.id == sub_goal_id).first()

    if not sub_goal:
        raise HTTPException(status_code=404, detail="Sub-goal not found")

    course = db.query(Course).filter(Course.project_id == sub_goal.project_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    sections = db.query(Section).filter(Section.course_id == course.id).all()

    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "sections": [
            {
                "id": section.id,
                "title": section.title,
                "content": section.content,
            }
            for section in sections
        ],
    }


def print_courses_and_lessons(db: Session):
    print("---- Listing all courses and sections with content ----")
    courses = db.query(Course).all()

    if not courses:
        print("No courses found.")
        return

    for course in courses:
        print(f"Course ID: {course.id}, Title: {course.title}")
        print(f"  Description: {course.description}\n")

        sections = db.query(Section).filter(Section.course_id == course.id).all()

        if sections:
            for section in sections:
                print(f"  Section ID: {section.id}, Title: {section.title}")
                print(f"    Content: {section.content}\n")
        else:
            print("  No sections found for this course.")
    print("----------------------------------------")
