from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud import meteorological_datum
from server.schemas import MeteorologicalDatum

router = APIRouter()


@router.get(RELATIVE_ROOT, response_model=list[MeteorologicalDatum])
async def get_meteorological_data(db_session: AsyncSession = Depends(get_db)):
    return await meteorological_datum.find_many(db_session=db_session)


# TODO: write out remaining query endpoints
