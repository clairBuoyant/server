from fastapi import APIRouter

from server.api.v1.endpoints import buoys, coastlines, meteorological_data, wave_data
from server.core.constants import (
    BUOYS_PATH,
    COASTLINES_PATH,
    METEOROLOGICAL_DATA_PATH,
    WAVE_DATA_PATH,
    PathTags,
)

# TODO: fastapi's jsonable_encoder VS PydanticModel.from_orm().dict()

api_router = APIRouter()

api_router.include_router(buoys.router, prefix=BUOYS_PATH, tags=[PathTags.BUOYS])
api_router.include_router(
    coastlines.router, prefix=COASTLINES_PATH, tags=[PathTags.COASTLINES]
)
api_router.include_router(
    meteorological_data.router,
    prefix=METEOROLOGICAL_DATA_PATH,
    tags=[PathTags.METEOROLOGICAL_DATA],
)
api_router.include_router(
    wave_data.router,
    prefix=WAVE_DATA_PATH,
    tags=[PathTags.WAVE_DATA],
)
