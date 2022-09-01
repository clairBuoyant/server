from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud.crud_wave_datum import wave_datum
from server.schemas.wave_datum import WaveDatum

router = APIRouter()


@router.get(RELATIVE_ROOT, response_model=list[WaveDatum])
async def get_meteorological_data(db_session: AsyncSession = Depends(get_db)):
    return await wave_datum.find_all(db=db_session)


# TODO: write out remaining query endpoints
