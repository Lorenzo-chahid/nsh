# tests/test_project_analyzer.py

import pytest
from app.services.project_analyzer import ProjectAnalyzer


@pytest.fixture
def project_analyzer():
    return ProjectAnalyzer(openai_api_key="your-openai-api-key")


def test_is_valid_description(project_analyzer):
    assert project_analyzer._is_valid_description("Build a web app") == True
    assert project_analyzer._is_valid_description("") == False
    assert project_analyzer._is_valid_description("Short") == False


def test_evaluate_difficulty(project_analyzer):
    sub_goals_easy = [
        {
            "name": "Setup",
            "skills": [{"name": "Basic HTML", "description": "easy skill"}],
        }
    ]
    sub_goals_intermediate = [
        {
            "name": "Backend Setup",
            "skills": [{"name": "SQL", "description": "advanced skill"}],
        }
    ] * 4
    sub_goals_hard = [
        {
            "name": "Complex AI Algorithm",
            "skills": [{"name": "Machine Learning", "description": "advanced skill"}],
        }
    ] * 7

    assert project_analyzer._evaluate_difficulty(sub_goals_easy) == 1
    assert project_analyzer._evaluate_difficulty(sub_goals_intermediate) == 2
    assert project_analyzer._evaluate_difficulty(sub_goals_hard) == 3


def test_check_feasibility(project_analyzer):
    sub_goals_feasible = [
        {"name": "Setup", "skills": [{"name": "Basic HTML", "time_to_learn": 10}]}
    ] * 10
    sub_goals_not_feasible = [
        {
            "name": "Complex AI Algorithm",
            "skills": [{"name": "Machine Learning", "time_to_learn": 50}],
        }
    ] * 5

    assert project_analyzer._check_feasibility(sub_goals_feasible) == True
    assert project_analyzer._check_feasibility(sub_goals_not_feasible) == False
