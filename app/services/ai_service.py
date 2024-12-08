import openai
import os
from app.schemas.ai_schemas import AIRequest
from app.db.models import User
import logging
from dotenv import load_dotenv

load_dotenv()


class AIService:
    @staticmethod
    async def generate_course_content(request: AIRequest, user: User):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            logging.error("Clé API OpenAI non configurée.")
            raise Exception("Clé API OpenAI non configurée.")

        openai.api_key = openai_api_key

        try:
            # Préparer le prompt pour l'IA
            prompt = (
                f"Vous êtes un assistant qui aide à créer des cours. {request.prompt}"
            )

            # Appel à l'API OpenAI
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=1500,
                n=1,
                stop=None,
                temperature=0.7,
            )

            ai_content = response.choices[0].text.strip()
            return ai_content

        except Exception as e:
            logging.error(f"Erreur lors de l'appel à l'API OpenAI : {str(e)}")
            raise e
