from fastapi import APIRouter

from server.api.v1.endpoints import buoys, coastlines, meteorological_datum
from server.core.constants import (  # WAVE_DATUM_PATH,
    BUOYS_PATH,
    COASTLINES_PATH,
    METEOROLOGICAL_DATUM_PATH,
    PathTags,
)

# TODO: fastapi's jsonable_encoder VS PydanticModel.from_orm().dict()

api_router = APIRouter()

api_router.include_router(buoys.router, prefix=BUOYS_PATH, tags=[PathTags.BUOYS])
api_router.include_router(
    coastlines.router, prefix=COASTLINES_PATH, tags=[PathTags.COASTLINES]
)
# TODO: add routher paths for meteorological and wave
api_router.include_router(
    meteorological_datum.router,
    prefix=METEOROLOGICAL_DATUM_PATH,
    tags=[PathTags.METEOROLOGICAL_DATUM],
)
