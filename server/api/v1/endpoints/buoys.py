from server.api.api_router import APIRouter
from server.api.dependencies import CurrentAsyncDBSession
from server.core.constants import RELATIVE_ROOT
from server.crud.crud_buoy import buoy
from server.schemas.buoy import Buoy

router = APIRouter()

# TODO: incorporate error handling


@router.get(RELATIVE_ROOT, response_model=list[Buoy])
async def get_buoys(db_session: CurrentAsyncDBSession):
    return await buoy.find_many(db_session=db_session)


@router.get("/{station_id}", response_model=Buoy)
async def get_buoy(
    station_id: str,
    db_session: CurrentAsyncDBSession,
):
    return await buoy.find_one(db_session=db_session, station_id=station_id)
