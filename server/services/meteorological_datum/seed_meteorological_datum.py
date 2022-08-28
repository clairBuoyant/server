from math import isnan

from pybuoy import Buoy
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.crud.crud_meteorological_datum import meteorological_datum
from server.schemas.meteorological_datum import MeteorologicalDatumCreate

# reference links:
# https://github.com/clairBuoyant/pybuoy/blob/main/docs/examples/get_realtime_data.py

buoy = Buoy()
STATION_ID = "44065"


async def seed_meteorological_data(db: AsyncSession):
    data = buoy.realtime.get(station_id=STATION_ID)
    # TODO: remove object from memory
    parsed_meteorological_data = [
        MeteorologicalDatumCreate(
            # TODO: refactor with the help of incoming pybuoy changes
            station_id=STATION_ID,
            date_recorded=datum[0].datetime,
            wind_direction=None if isnan(datum[0].value) else datum[0].value,
            wind_speed=None if isnan(datum[1].value) else datum[1].value,
            wind_gust=None if isnan(datum[2].value) else datum[2].value,
            wave_height=None if isnan(datum[3].value) else datum[3].value,
            dominant_wave_period=None if isnan(datum[4].value) else datum[4].value,
            average_wave_period=None if isnan(datum[5].value) else datum[5].value,
            wave_direction=None if isnan(datum[6].value) else datum[6].value,
            sea_level_pressure=None if isnan(datum[7].value) else datum[7].value,
            pressure_tendency=None if isnan(datum[8].value) else datum[8].value,
            air_temperature=None if isnan(datum[9].value) else datum[9].value,
            water_temperature=None if isnan(datum[10].value) else datum[10].value,
            dewpoint_temperature=None if isnan(datum[11].value) else datum[11].value,
            visibility=None if isnan(datum[12].value) else datum[12].value,
            tide=None if isnan(datum[13].value) else datum[13].value,
        )
        for datum in data
    ]
    return await meteorological_datum.create_meteorological_datum(
        db, parsed_meteorological_data
    )
