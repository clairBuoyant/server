from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

API_V1_STR = "/api/v1"


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
