from enum import Enum


class PythonEnv(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


API_VERSION = "v1"
DEFAULT_PYTHON_ENV = PythonEnv.PRODUCTION
