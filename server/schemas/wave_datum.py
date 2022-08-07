from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class WaveBase(BaseModel):
    station_id: str
    date_recorded: datetime
    wave_height: Optional[float]
    swell_height: Optional[float]
    swell_period: Optional[float]
    wind_wave_height: Optional[float]
    wind_wave_period: Optional[float]
    swell_direction: Optional[str]
    wind_wave_direction: Optional[str]
    steepness: Optional[str]
    average_wave_period: Optional[float]


# Properties to receive on item creation
class WaveCreate(WaveBase):
    ...


# Properties to receive on item update
class WaveUpdate(WaveBase):
    ...


# Properties shared by models stored in DB
class WaveInDBBase(WaveBase):
    id: int

    class Config:
        orm_mode = True


class Wave(WaveInDBBase):
    ...


# Properties properties stored in DB
class WaveInDB(WaveInDBBase):
    ...
