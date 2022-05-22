from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from server.crud.base import CRUDBase
from server.models.buoy import Buoy
from server.schemas.buoy import BuoyCreate, BuoyUpdate


# TODO: Rework with OOP composition
class CRUDBuoy(CRUDBase[Buoy, BuoyCreate, BuoyUpdate]):
    @staticmethod
    async def get_buoy(db_session: AsyncSession, station_id: str):
        return await db_session.execute(
            select(Buoy).where(Buoy.station_id == station_id)
        )

    @staticmethod
    async def create_buoys(db_session: AsyncSession, buoys: list[BuoyCreate]):
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
                water_quality=buoy.waterquality,
                dart=buoy.dart,
                seq=buoy.seq,
            )
            for buoy in buoys
        ]
        db_session.add_all(buoys_to_db)
        await db_session.commit()


buoy = CRUDBuoy(Buoy)
