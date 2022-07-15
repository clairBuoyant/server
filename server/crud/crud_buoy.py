from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from server.crud.base import CRUDBase
from server.models.buoy import Buoy
from server.schemas.buoy import BuoyCreate, BuoyUpdate


class CRUDBuoy(CRUDBase[Buoy, BuoyCreate, BuoyUpdate]):
    async def find_one(self, db: AsyncSession, station_id: str):
        result = await db.execute(select(Buoy).where(Buoy.station_id == station_id))
        return result.scalars().first()

    async def create_buoys(self, db: AsyncSession, buoys: list[BuoyCreate]):
        buoys_to_db = [
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
        ]
        db.add_all(buoys_to_db)
        await db.commit()


buoy = CRUDBuoy(Buoy)
