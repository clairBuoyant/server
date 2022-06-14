from enum import Enum

_API_VERSION = "v1"
API_PREFIX = f"/api/{_API_VERSION}"

BUOYS_PATH = "/buoys"
COASTLINES_PATH = "/coastlines"

BUOYS_URI = f"{API_PREFIX}{BUOYS_PATH}"
COASTLINES_URI = f"{API_PREFIX}{COASTLINES_PATH}"

RELATIVE_ROOT = "/"


class PathTags(Enum):
    BUOYS = "buoys"
    COASTLINES = "coastlines"


class PythonEnv(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


DEFAULT_PYTHON_ENV = PythonEnv.PRODUCTION
