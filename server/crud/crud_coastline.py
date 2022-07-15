from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from server.crud.base import CRUDBase
from server.models.coastline import Coastline
from server.schemas.coastline import CoastlineCreate, CoastlineUpdate


class CRUDCoastline(CRUDBase[Coastline, CoastlineCreate, CoastlineUpdate]):
    async def create_coastlines(
        self, db_session: AsyncSession, coastlines: list[CoastlineCreate]
    ):
        coastlines_to_db = [
            Coastline(station_id=coastline.station_id, geom=coastline.geom)
            for coastline in coastlines
        ]
        db_session.add_all(coastlines_to_db)
        await db_session.commit()

    async def get_coastlines(self, db_session: AsyncSession):
        # `selectinload`: alternative approach to `joinedload`
        stmt = (
            select(Coastline)
            .options(joinedload(Coastline.buoy, innerjoin=True))
            .order_by(Coastline.id)
        )
        results = await db_session.execute(stmt)
        return results.scalars().all()


coastline = CRUDCoastline(Coastline)
