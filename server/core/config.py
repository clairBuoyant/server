from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

API_V1_STR = "/api/v1"
COASTLINES_V1_STR = "%s/coastlines" % API_V1_STR


class Settings(BaseSettings):
    DATABASE_URL: str
    # TODO add tags lsit for future development
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
