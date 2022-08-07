from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class MeteorologicalDatumBase(BaseModel):
    station_id: str
    date_recorded: datetime
    wind_direction: Optional[int]
    wind_speed: Optional[float]
    wind_gust: Optional[float]
    wave_height: Optional[float]
    dominant_period: Optional[int]
    average_wave_period: Optional[float]
    wave_direction: Optional[str]
    air_pressure: Optional[float]
    pressure_tendency: Optional[float]
    air_temperature: Optional[float]
    water_temperature: Optional[float]
    dewpoint_temperature: Optional[float]
    visibility: Optional[float]
    tide: Optional[float]


# Properties to receive on item creation
class MeteorologicalDatumCreate(MeteorologicalDatumBase):
    ...


# Properties to receive on item update
class MeteorologicalDatumUpdate(MeteorologicalDatumBase):
    ...


# Properties shared by models stored in DB
class MeteorologicalDatumInDBBase(MeteorologicalDatumBase):
    id: int

    class Config:
        orm_mode = True


class MeteorologicalDatum(MeteorologicalDatumInDBBase):
    ...


# Properties properties stored in DB
class MeteorologicalInDB(MeteorologicalDatumInDBBase):
    ...
