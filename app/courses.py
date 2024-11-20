# app/api/v1/courses.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.course_schemas import CourseCreate, CourseResponse
from app.services.course_service import create_course, get_courses
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=CourseResponse)
def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db, course)


@router.get("/", response_model=list[CourseResponse])
def list_courses(db: Session = Depends(get_db)):
    return get_courses(db)
