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

    results = await coastline.async_get(db_session, id=1)
    # print("RESULTS", schemas.Coastline.from_orm(next(results.chunks(None))[0]).dict())
    for row in results:
        print(schemas.Coastline.from_orm(row.Coastline).dict())

    # stmt = (
    #     select(models.Coastline)
    #     .options(joinedload(models.Coastline.buoy, innerjoin=True))
    #     .order_by(models.Coastline.id)
    # )
    # response = await db_session.execute(stmt)

    # return [schemas.Coastline.from_orm(row.Coastline).dict() for row in response]
    return "Work in progress"
