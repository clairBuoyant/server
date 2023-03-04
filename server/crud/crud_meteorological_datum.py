from sqlalchemy.ext.asyncio import AsyncSession

from server.crud.base import CRUDBase
from server.models import MeteorologicalDatum
from server.schemas import MeteorologicalDatumCreate, MeteorologicalDatumUpdate


class CRUDMeteorologicalDatum(
    CRUDBase[MeteorologicalDatum, MeteorologicalDatumCreate, MeteorologicalDatumUpdate]
):
    async def create_many(
        self, db_session: AsyncSession, data: list[MeteorologicalDatumCreate]
    ):
        return await super().create_many(
            db_session,
            [
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
            ],
        )


meteorological_datum = CRUDMeteorologicalDatum(MeteorologicalDatum)
