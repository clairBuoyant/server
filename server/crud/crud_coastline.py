from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from server.crud.base import CRUDBase
from server.models.coastline import Coastline
from server.schemas.coastline import CoastlineCreate, CoastlineUpdate


# TODO: Rework with OOP composition
class CRUDCoastline(CRUDBase[Coastline, CoastlineCreate, CoastlineUpdate]):
    # TODO: Create get method

    async def create_coastlines(
        db_session: AsyncSession, coastlines: list[CoastlineCreate]
    ):
        coastlines_to_db = [
            Coastline(station_id=coastline.station_id, geom=coastline.geom)
            for coastline in coastlines
        ]
        db_session.add_all(coastlines_to_db)
        await db_session.commit()

    async def get_coastlines(db_session: AsyncSession):
        # `selectinload`: alternative approach to `joinedload`
        stmt = (
            select(Coastline)
            .options(joinedload(Coastline.buoy, innerjoin=True))
            .order_by(Coastline.id)
        )
        return await db_session.execute(stmt)


coastline = CRUDCoastline(Coastline)
