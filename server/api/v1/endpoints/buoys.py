from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud.crud_buoy import buoy
from server.schemas.buoy import Buoy

router = APIRouter()

# TODO: incorporate error handling


@router.get(RELATIVE_ROOT, response_model=list[Buoy])
async def get_buoys(db_session: AsyncSession = Depends(get_db)):
    return await buoy.find_many(db_session=db_session)


@router.get("/{station_id}", response_model=Buoy)
async def get_buoy(
    station_id: str,
    db_session: AsyncSession = Depends(get_db),
):
    return await buoy.find_one(db_session=db_session, station_id=station_id)
