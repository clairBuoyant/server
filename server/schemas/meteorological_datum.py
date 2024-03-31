from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# Shared properties
class MeteorologicalDatumBase(BaseModel):
    station_id: str
    date_recorded: datetime
    wind_direction: Optional[int] = None
    wind_speed: Optional[float] = None
    wind_gust: Optional[float] = None
    wave_height: Optional[float] = None
    dominant_wave_period: Optional[float] = None
    average_wave_period: Optional[float] = None
    wave_direction: Optional[int] = None
    sea_level_pressure: Optional[float] = None
    pressure_tendency: Optional[float] = None
    air_temperature: Optional[float] = None
    water_temperature: Optional[float] = None
    dewpoint_temperature: Optional[float] = None
    visibility: Optional[float] = None
    tide: Optional[float] = None


# Properties to receive on item creation
class MeteorologicalDatumCreate(MeteorologicalDatumBase): ...


# Properties to receive on item update
class MeteorologicalDatumUpdate(MeteorologicalDatumBase): ...


# Properties shared by models stored in DB
class MeteorologicalDatumInDBBase(MeteorologicalDatumBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class MeteorologicalDatum(MeteorologicalDatumInDBBase): ...


# Properties properties stored in DB
class MeteorologicalDatumInDB(MeteorologicalDatumInDBBase): ...
