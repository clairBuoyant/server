from pybuoy import Buoy
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.crud.crud_wave_datum import wave_datum
from server.schemas.wave_datum import WaveDatumCreate

buoy = Buoy()
STATION_ID = "44065"


async def seed_wave_data(db_session: AsyncSession, station_id: str = STATION_ID):
    data = buoy.realtime.get(station_id=station_id, dataset="spec")
    parsed_wave_data = [
        WaveDatumCreate(
            station_id=station_id,
            date_recorded=datum.datetime,
            significant_wave_height=datum.significant_wave_height.value,
            swell_height=datum.swell_height.value,
            swell_period=datum.swell_period.value,
            wind_wave_height=datum.wind_wave_height.value,
            wind_wave_period=datum.wind_wave_period.value,
            swell_direction=datum.swell_direction.value,
            wind_wave_direction=datum.wind_wave_direction.value,
            steepness=datum.steepness.value,
            average_wave_period=datum.average_wave_period.value,
            mean_wave_direction=datum.dominant_wave_direction.value,
        )
        for datum in data
    ]
    return await wave_datum.create_many(db_session, parsed_wave_data)
