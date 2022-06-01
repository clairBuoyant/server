from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

API_V1_STR = "/api/v1"
COASTLINES_V1_STR = API_V1_STR + "coastlines"


class Settings(BaseSettings):
    DATABASE_URL: str
    API_V1_ROUTE: str = API_V1_STR
    COASTLINES_V1_ROUTE: str = COASTLINES_V1_STR
    #TODO add tags lsit for future development
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
