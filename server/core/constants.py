from enum import Enum

_API_VERSION = "v1"
_API_PREFIX = f"api/{_API_VERSION}"


buoys_path = f"{_API_PREFIX}/buoys"
coastlines_path = f"{_API_PREFIX}/coastlines"


class PythonEnv(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


DEFAULT_PYTHON_ENV = PythonEnv.PRODUCTION
