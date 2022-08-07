from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud.crud_meteorological_datum import meteorological_datum
from server.schemas.meteorological_datum import MeteorologicalDatum

router = APIRouter()

# TODO: build out meteorological endpoint


@router.get(RELATIVE_ROOT, response_model=list[MeteorologicalDatum])
async def get_meteorological_datum(db_session: AsyncSession = Depends(get_db)):
    return await meteorological_datum.find_all(db=db_session)
