from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from server import models, schemas
from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT

router = APIRouter()

# TODO: incorporate error handling and refactor with CRUDBuoy
# TODO: incorporate response_model and response type


@router.get(RELATIVE_ROOT)
async def get_buoys(db_session: AsyncSession = Depends(get_db)):
    stmt = select(models.Buoy)
    response = await db_session.execute(stmt)

    return [schemas.Buoy.from_orm(row.Buoy).dict() for row in response]


@router.get("/{station_id}")
async def get_buoy(
    station_id: str,
    db_session: AsyncSession = Depends(get_db),
):
    stmt = select(models.Buoy).where(models.Buoy.station_id == station_id)
    response = await db_session.execute(stmt)
    buoy = response.first()

    return schemas.Buoy.from_orm(buoy.Buoy).dict()
