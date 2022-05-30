from functools import lru_cache

from pydantic import BaseSettings

from server.core.constants import DEFAULT_PYTHON_ENV

API_V1_STR = "/api/v1"
COASTLINES_V1_STR = "%s/coastlines" % API_V1_STR


class Settings(BaseSettings):
    DATABASE_URL: str
    PYTHON_ENV: str = DEFAULT_PYTHON_ENV

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():  # pragma: no cover
    return Settings()
