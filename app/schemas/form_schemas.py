# app/schemas/form_schemas.py

from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from app.schemas.course_schemas import CourseResponse


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    duration: int
    category: str
    created_at: datetime
    user_id: int
    custom_inputs: Optional[dict] = None
    courses: Optional[List[CourseResponse]] = []
    generated_plan: Optional[str] = None  # Assurez-vous que ce champ est inclus

    class Config:
        from_attributes = True  # Pour la compatibilité avec les modèles ORM


class WeightLossForm(BaseModel):
    goal_weight: float
    current_weight: float
    daily_calories: int
    exercise_level: str
    duration: int


class StressManagementForm(BaseModel):
    stress_level: int
    coping_mechanisms: str
    exercise_level: str
    duration: int


class BudgetForm(BaseModel):
    income: float
    expenses: float
    savings_goal: float
    duration: int


class BusinessForm(BaseModel):
    business_name: str
    business_goal: str
    projected_income: float
    duration: int


class LanguageLearningForm(BaseModel):
    language: str
    current_level: str
    learning_method: str
    duration: int
