from functools import lru_cache

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from .constants import DEFAULT_PYTHON_ENV

class Settings(BaseSettings):
    DATABASE_URL: str
    PYTHON_ENV: str = DEFAULT_PYTHON_ENV.value
    model_config = ConfigDict(env_file=".env")


@lru_cache()
def get_settings():  # pragma: no cover
    return Settings()
