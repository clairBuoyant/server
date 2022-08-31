from datetime import datetime as dt

from pybuoy import Buoy
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.crud.crud_wave_datum import wave_datum
from server.schemas.wave_datum import WaveDatumCreate

buoy = Buoy()
STATION_ID = "44065"

data = buoy.realtime.get(station_id=STATION_ID, dataset="spec")


async def seed_wave_data(db: AsyncSession):
    rows = data.strip().split("\n")
    parsed_wave_data = []
    for row in rows[2:]:
        record_array = " ".join(row.split()).split(" ")
        parsed_wave_data.append(
            WaveDatumCreate(
                station_id=STATION_ID,
                date_recorded=dt(
                    int(record_array[0]),
                    int(record_array[1]),
                    int(record_array[2]),
                    int(record_array[3]),
                    int(record_array[4]),
                ),
                significant_wave_height=record_array[5],
                swell_height=record_array[6],
                swell_period=None if record_array[7] == "MM" else record_array[7],
                wind_wave_height=record_array[8],
                wind_wave_period=record_array[9],
                swell_direction=None if record_array[10] == "MM" else record_array[10],
                wind_wave_direction=record_array[11],
                steepness=None if record_array[12] == "N/A" else record_array[12],
                average_wave_period=record_array[13],
                mean_wave_direction=record_array[14],
            )
        )
    return await wave_datum.create_wave_data(db, parsed_wave_data)
