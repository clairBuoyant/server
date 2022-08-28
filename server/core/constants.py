from enum import Enum

_API_VERSION = "v1"
API_PREFIX = f"/api/{_API_VERSION}"

BUOYS_PATH = "/buoys"
COASTLINES_PATH = "/coastlines"
METEOROLOGICAL_DATA_PATH = "/meteorological_data"
WAVE_DATA_PATH = "/wave_data"

BUOYS_URI = f"{API_PREFIX}{BUOYS_PATH}"
COASTLINES_URI = f"{API_PREFIX}{COASTLINES_PATH}"
METEOROLOGICAL_DATA_URI = f"{API_PREFIX}{METEOROLOGICAL_DATA_PATH}"
WAVE_DATA_URI = f"{API_PREFIX}{WAVE_DATA_PATH}"

RELATIVE_ROOT = "/"


class PathTags(Enum):
    BUOYS = "buoys"
    COASTLINES = "coastlines"
    METEOROLOGICAL_DATA = "meteorological_data"


class PythonEnv(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


DEFAULT_PYTHON_ENV = PythonEnv.PRODUCTION
