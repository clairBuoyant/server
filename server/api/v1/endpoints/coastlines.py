from server.api.api_router import APIRouter
from server.api.dependencies import CurrentAsyncDBSession
from server.core.constants import RELATIVE_ROOT
from server.crud import coastline
from server.schemas import Coastline

router = APIRouter()

# TODO: incorporate error handling


@router.get(RELATIVE_ROOT, response_model=list[Coastline])
async def get_coastlines(db_session: CurrentAsyncDBSession):
    return await coastline.find_many(db_session)


@router.get("/{coastline_id}", response_model=Coastline)
async def get_coastline(coastline_id: int, db_session: CurrentAsyncDBSession):
    return await coastline.find_one(db_session, id=coastline_id)
