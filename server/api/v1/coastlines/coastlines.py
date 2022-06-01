from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from server import models, schemas
# TODO Implement Settings to have hardcoded route prefixes for future use
from server.core.config import Settings
from server.db.session import get_db

router = APIRouter(prefix="/api/v1/coastlines", tags=["coastlines"])


@router.get("/")
async def get_coastlines(
    db_session: AsyncSession = Depends(get_db),
) -> models.Coastline:

    # `selectinload`: alternative approach to `joinedload`
    stmt = (
        select(models.Coastline)
        .options(joinedload(models.Coastline.buoy, innerjoin=True))
        .order_by(models.Coastline.id)
    )
    response = await db_session.execute(stmt)

    """TODO
    * Add error handling
    """
    return [schemas.Coastline.from_orm(row.Coastline).dict() for row in response]
