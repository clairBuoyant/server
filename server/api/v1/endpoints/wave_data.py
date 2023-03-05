from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.api_router import APIRouter
from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud.crud_wave_datum import wave_datum
from server.schemas.wave_datum import WaveDatum

router = APIRouter()


@router.get(RELATIVE_ROOT, response_model=list[WaveDatum])
async def get_wave_data(db_session: AsyncSession = Depends(get_db)):
    return await wave_datum.find_many(db_session=db_session)


# TODO: write out remaining query endpoints
