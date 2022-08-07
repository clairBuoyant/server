from enum import Enum

_API_VERSION = "v1"
API_PREFIX = f"/api/{_API_VERSION}"

BUOYS_PATH = "/buoys"
COASTLINES_PATH = "/coastlines"
METEOROLOGICAL_DATUM_PATH = "/meteorological_datum"
WAVE_DATUM_PATH = "/wave_datum"

BUOYS_URI = f"{API_PREFIX}{BUOYS_PATH}"
COASTLINES_URI = f"{API_PREFIX}{COASTLINES_PATH}"
METEOROLOGICAL_DATUM_URI = f"{API_PREFIX}{METEOROLOGICAL_DATUM_PATH}"
WAVE_DATUM_URI = f"{API_PREFIX}{WAVE_DATUM_PATH}"

RELATIVE_ROOT = "/"


class PathTags(Enum):
    BUOYS = "buoys"
    COASTLINES = "coastlines"
    METEOROLOGICAL_DATUM = "meteorological_datum"


class PythonEnv(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


DEFAULT_PYTHON_ENV = PythonEnv.PRODUCTION
