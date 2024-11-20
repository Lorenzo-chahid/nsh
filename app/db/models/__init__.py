# app/db/models/__init__.py

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Importez tous les modèles ici pour qu'ils soient connus de SQLAlchemy
from .user import User
from .admin import Admin
from .event import Event
from .event_participant import EventParticipant, ParticipantStatus
from .notification import Notification, NotificationType
from .project import Project
from .quest import Quest
from .skill import Skill
from .skill_tree import SkillTree
from .ia_state import IAState
from .course import Course
from .section import Section
from .exercise import Exercise
from .user_exercise import UserExercise
from .user_course_progress import UserCourseProgress
from .user_section_progress import UserSectionProgress
from .user_project import UserProject
from .comment import Comment
from .sub_goal import SubGoal
from .message import (
    messages,
)  # Si vous avez une table messages définie en tant que Table
