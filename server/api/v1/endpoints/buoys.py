from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from server import models, schemas
from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud import buoy

router = APIRouter()

# TODO: incorporate error handling
# TODO: incorporate response_model and response type


@router.get(RELATIVE_ROOT)
async def get_buoys(db_session: AsyncSession = Depends(get_db)):
    buoys_response = await buoy.find_many(db=db_session)
    return [schemas.Buoy.from_orm(row.Buoy).dict() for row in buoys_response]


@router.get("/{station_id}")
async def get_buoy(
    station_id: str,
    db_session: AsyncSession = Depends(get_db),
):
    buoy_response = await buoy.find_one(db=db_session, station_id=station_id)
    return schemas.Buoy.from_orm(buoy_response.Buoy).dict()
