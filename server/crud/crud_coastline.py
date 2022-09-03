from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from sqlalchemy.future import select  # type: ignore
from sqlalchemy.orm import joinedload  # type: ignore

from server.crud.base import CRUDBase
from server.models.coastline import Coastline
from server.schemas.coastline import CoastlineCreate, CoastlineUpdate


class CRUDCoastline(CRUDBase[Coastline, CoastlineCreate, CoastlineUpdate]):
    async def create_many(
        self, db_session: AsyncSession, coastlines: list[CoastlineCreate]
    ):
        return await super().create_many(
            db_session,
            [
                Coastline(station_id=coastline.station_id, geom=coastline.geom)
                for coastline in coastlines
            ],
        )

    async def get_coastlines(self, db_session: AsyncSession):
        # `selectinload`: alternative approach to `joinedload`
        stmt = (
            select(self.model)
            .options(joinedload(self.model.buoy, innerjoin=True))
            .order_by(self.model.id)
        )
        results = await db_session.execute(stmt)
        return results.scalars().all()


coastline = CRUDCoastline(Coastline)
