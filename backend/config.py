import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "Context-Aware Financial Explainer"
    API_V1_STR = "/api/v1"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
