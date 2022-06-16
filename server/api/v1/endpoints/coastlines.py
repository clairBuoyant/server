from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from server import models, schemas
from server.api.dependencies import get_db
from server.core.constants import RELATIVE_ROOT
from server.crud.crud_coastline import coastline

router = APIRouter()

# TODO: incorporate error handling and refactor with CRUDCoastline
# TODO: incorporate response_model and response type


@router.get(RELATIVE_ROOT)
async def get_coastlines(
    db_session: AsyncSession = Depends(get_db),
) -> models.Coastline:

    # TODO: finish get_coastlines with CoastlineCRUD
    response = await coastline.async_get(db_session)

    return [schemas.Coastline.from_orm(row.Coastline).dict() for row in response]


@router.get("/{coastline_id}")
async def get_coastline(
    coastline_id: int,
    db_session: AsyncSession = Depends(get_db),
) -> models.Coastline:

    # TODO: create tests
    response = await coastline.async_get_single(db_session, id=coastline_id)
    coastline_from_response = response.first()
    return schemas.Coastline.from_orm(coastline_from_response.Coastline).dict()
