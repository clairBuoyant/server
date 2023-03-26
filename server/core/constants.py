from enum import Enum

_API_VERSION = "v1"
API_PREFIX = f"/api/{_API_VERSION}"

BUOYS_PATH = "/buoys"
COASTLINES_PATH = "/coastlines"
FORECASTS_PATH = "/forecasts"
METEOROLOGICAL_DATA_PATH = "/meteorological_data"
WAVE_DATA_PATH = "/wave_data"

BUOYS_URI = f"{API_PREFIX}{BUOYS_PATH}"
COASTLINES_URI = f"{API_PREFIX}{COASTLINES_PATH}"
FORECASTS_URI = f"{API_PREFIX}{FORECASTS_PATH}"
METEOROLOGICAL_DATA_URI = f"{API_PREFIX}{METEOROLOGICAL_DATA_PATH}"
WAVE_DATA_URI = f"{API_PREFIX}{WAVE_DATA_PATH}"

RELATIVE_ROOT = "/"


class PathTags(Enum):
    BUOYS = "buoys"
    COASTLINES = "coastlines"
    FORECASTS = "forecasts"
    METEOROLOGICAL_DATA = "meteorological_data"
    WAVE_DATA = "wave_data"


class PythonEnv(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


DEFAULT_PYTHON_ENV = PythonEnv.PRODUCTION
