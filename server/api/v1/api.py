from fastapi import APIRouter

from server.api.v1.endpoints import buoys, coastlines
from server.core.constants import BUOYS_PATH, COASTLINES_PATH, PathTags

# TODO: JSON serialization with fastapi's `jsonable_encoder` VS PydanticModel.from_orm().dict()

api_router = APIRouter()

api_router.include_router(buoys.router, prefix=BUOYS_PATH, tags=[PathTags.BUOYS])
api_router.include_router(
    coastlines.router, prefix=COASTLINES_PATH, tags=[PathTags.COASTLINES]
)
