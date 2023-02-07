from pybuoy import Buoy
from sqlalchemy.ext.asyncio import AsyncSession

from server.crud import meteorological_datum
from server.schemas import MeteorologicalDatumCreate

buoy = Buoy()
STATION_ID = "44065"


async def seed_meteorological_data(
    db_session: AsyncSession, station_id: str = STATION_ID
):
    data = buoy.realtime.get(station_id=station_id)
    # TODO: remove object from memory
    parsed_meteorological_data = [
        MeteorologicalDatumCreate(
            station_id=station_id,
            date_recorded=datum.datetime,
            wind_direction=datum.wind_direction.value,
            wind_speed=datum.wind_speed.value,
            wind_gust=datum.wind_gust.value,
            wave_height=datum.wave_height.value,
            dominant_wave_period=datum.dominant_wave_period.value,
            average_wave_period=datum.average_wave_period.value,
            wave_direction=datum.wave_direction.value,
            sea_level_pressure=datum.sea_level_pressure.value,
            pressure_tendency=datum.pressure_tendency.value,
            air_temperature=datum.air_temperature.value,
            water_temperature=datum.water_temperature.value,
            dewpoint_temperature=datum.dewpoint_temperature.value,
            visibility=datum.visibility.value,
            tide=datum.tide.value,
        )
        for datum in data
    ]
    return await meteorological_datum.create_many(
        db_session, parsed_meteorological_data
    )
