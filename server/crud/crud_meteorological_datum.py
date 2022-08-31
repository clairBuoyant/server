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
            select(self.model).where(MeteorologicalDatum.date_recorded == date_recorded)
        )
        return result.scalars().first()

    async def find_all(self, db: AsyncSession):
        result = await db.execute(select(self.model))
        return result.scalars().all()

    # TODO: Try to refactor this to follow DRY principle
    async def find_many_recordings(
        self,
        db: AsyncSession,
        station_id: str,
        begin_date: datetime,
        end_date: datetime,
    ):
        result = await db.execute(
            select(self.model).where(
                self.model.station_id == station_id
                and self.model.date_recorded >= begin_date
                and self.model.date_recorded <= end_date
            )
        )
        return result

    async def create_many(
        self, db: AsyncSession, data: list[MeteorologicalDatumCreate]
    ):
        data_to_db = [
            MeteorologicalDatum(
                station_id=datum.station_id,
                date_recorded=datum.date_recorded,
                wind_direction=datum.wind_direction,
                wind_speed=datum.wind_speed,
                wind_gust=datum.wind_gust,
                wave_height=datum.wave_height,
                dominant_wave_period=datum.dominant_wave_period,
                average_wave_period=datum.average_wave_period,
                wave_direction=datum.wave_direction,
                sea_level_pressure=datum.sea_level_pressure,
                pressure_tendency=datum.pressure_tendency,
                air_temperature=datum.air_temperature,
                water_temperature=datum.water_temperature,
                dewpoint_temperature=datum.dewpoint_temperature,
                visibility=datum.visibility,
                tide=datum.tide,
            )
            for datum in data
        ]
        db.add_all(data_to_db)
        await db.commit()


meteorological_datum = CRUDMeteorologicalDatum(MeteorologicalDatum)
