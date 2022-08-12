from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud import coastline
from server.schemas import Coastline

router = APIRouter()

# TODO: incorporate error handling


@router.get(RELATIVE_ROOT, response_model=list[Coastline])
async def get_coastlines(db_session: AsyncSession = Depends(get_db)):
    return await coastline.find_many(db_session)


@router.get("/{coastline_id}", response_model=Coastline)
async def get_coastline(coastline_id: int, db_session: AsyncSession = Depends(get_db)):
    return await coastline.find_one(db_session, id=coastline_id)
