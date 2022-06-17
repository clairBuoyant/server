from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server import models, schemas
from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud import coastline

router = APIRouter()

# TODO: incorporate error handling
# TODO: incorporate response_model and response type


@router.get(RELATIVE_ROOT)
async def get_coastlines(
    db_session: AsyncSession = Depends(get_db),
) -> models.Coastline:

    response = await coastline.find_many(db_session)
    return [schemas.Coastline.from_orm(row.Coastline).dict() for row in response]


@router.get("/{coastline_id}")
async def get_coastline(
    coastline_id: int,
    db_session: AsyncSession = Depends(get_db),
) -> models.Coastline:

    coastline_from_response = await coastline.find_one(db_session, id=coastline_id)
    return schemas.Coastline.from_orm(coastline_from_response.Coastline).dict()
