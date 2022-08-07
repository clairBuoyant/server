from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from sqlalchemy.future import select  # type: ignore

from server.crud.base import CRUDBase
from server.models.meteorological_datum import MeteorologicalDatum
from server.schemas.meteorological_datum import (
    MeteorologicalDatumCreate,
    MeteorologicalDatumUpdate,
)


class CRUDMeteorologicalDatum(
    CRUDBase[MeteorologicalDatum, MeteorologicalDatumCreate, MeteorologicalDatumUpdate]
):
    async def find_one(self, db: AsyncSession, date_recorded: datetime):
        result = await db.execute(
            select(MeteorologicalDatum).where(
                MeteorologicalDatum.date_recorded == date_recorded
            )
        )
        return result.scalars().first()

    async def find_all(self, db: AsyncSession):
        return await db.execute(select(MeteorologicalDatum))

    # TODO: Try to refactor this to follow DRY principle
    async def find_many_recordings(
        self,
        db: AsyncSession,
        station_id: str,
        begin_date: datetime,
        end_date: datetime,
    ):
        result = await db.execute(
            select(MeteorologicalDatum).where(
                MeteorologicalDatum.station_id == station_id
                and MeteorologicalDatum.date_recorded >= begin_date
                and MeteorologicalDatum.date_recorded <= end_date
            )
        )
        return result

    async def create_meteorological_datum(
        self, db: AsyncSession, datum: list[MeteorologicalDatumCreate]
    ):
        data_to_db = [
            MeteorologicalDatum(
                station_id=data.station_id,
                date_recorded=data.date_recorded,
                wind_direction=data.wind_direction,
                wind_speed=data.wind_speed,
                wind_gust=data.wind_gust,
                wave_height=data.wave_height,
                dominant_period=data.dominant_period,
                average_wave_period=data.average_wave_period,
                wave_direction=data.mean_wave_direction,
                air_pressure=data.air_pressure,
                pressure_tendency=data.pressure_tendency,
                air_temperature=data.air_temperature,
                water_temperature=data.water_temperature,
                dewpoint_temperature=data.dewpoint,
                visibility=data.visibility,
                tide=data.tide,
            )
            for data in datum
        ]
        db.add_all(data_to_db)
        await db.commit()


meteorological_datum = CRUDMeteorologicalDatum(MeteorologicalDatum)
