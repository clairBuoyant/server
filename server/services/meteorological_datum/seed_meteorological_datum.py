from pybuoy import Buoy
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.crud.crud_meteorological_datum import meteorological_datum
from server.schemas.meteorological_datum import MeteorologicalDatumCreate

# reference links:
# https://github.com/clairBuoyant/pybuoy/blob/main/docs/examples/get_realtime_data.py

buoy = Buoy()
STATION_ID = "44065"

datum = buoy.realtime.get(station_id=STATION_ID)


async def seed_meteorological_data(db: AsyncSession):
    parsed_meteorological_data = [
        MeteorologicalDatumCreate(
            station_id=STATION_ID,
            date_recorded=data[0].datetime,
            wind_direction=data[0].value,
            wind_speed=data[1].value,
            wind_gust=data[2].value,
            wave_height=data[3].value,
            dominant_wave_period=data[4].value,
            average_wave_period=data[5].value,
            wave_direction=data[6].value,
            air_pressure=data[7].value,
            pressure_tendency=data[8].value,
            air_temperature=data[9].value,
            water_temperature=data[10].value,
            dewpoint_temperature=data[11].value,
            visibility=data[12].value,
            tide=data[13].value,
        )
        for data in datum
    ]
    return await meteorological_datum.create_meteorological_datum(
        db, parsed_meteorological_data
    )
