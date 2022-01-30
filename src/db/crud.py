from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models, schemas


async def get_buoy(db: AsyncSession, station_id: str):
    buoy = None
    async with db.begin() as conn:
        stmt = select(models.Buoy).where(models.Buoy.station_id == station_id)
        result = await conn.execute(stmt)
        buoy = result.one_or_none()
    await db.dispose()
    return buoy


async def create_buoys(db: AsyncSession, buoys: list[schemas.BuoyCreate]):
    buoys_to_db = []
    for buoy in buoys:
        buoys_to_db.append(
            models.Buoy(
                station_id=buoy.station_id,
                name=buoy.name,
                owner=buoy.owner,
                location=buoy.location,
                elev=buoy.elev,
                pgm=buoy.pgm,
                type=buoy.buoy_type,
                met=buoy.met,
                currents=buoy.currents,
                water_quality=buoy.waterquality,
                dart=buoy.dart,
                seq=buoy.seq,
            )
        )
    async with AsyncSession(db) as session:
        async with session.begin():
            session.add_all(buoys_to_db)
        await session.commit()
    await db.dispose()
