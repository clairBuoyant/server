from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from server.crud.base import CRUDBase
from server.models.buoy import Buoy
from server.schemas.buoy import BuoyCreate, BuoyUpdate


class CRUDBuoy(CRUDBase[Buoy, BuoyCreate, BuoyUpdate]):
    async def find_one(self, db_session: AsyncSession, station_id: str):
        result = await db_session.execute(
            select(self.model).where(self.model.station_id == station_id)
        )
        return result.scalars().first()

    async def create_many(self, db_session: AsyncSession, buoys: list[BuoyCreate]):
        return await super().create_many(
            db_session,
            [
                Buoy(
                    station_id=buoy.station_id,
                    name=buoy.name,
                    owner=buoy.owner,
                    location=buoy.location,
                    elev=buoy.elev,
                    pgm=buoy.pgm,
                    type=buoy.type,
                    met=buoy.met,
                    currents=buoy.currents,
                    water_quality=buoy.water_quality,
                    dart=buoy.dart,
                    seq=buoy.seq,
                )
                for buoy in buoys
            ],
        )


buoy = CRUDBuoy(Buoy)
