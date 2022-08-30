from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class WaveDatumBase(BaseModel):
    station_id: str
    date_recorded: datetime
    significant_wave_height: Optional[float]
    swell_height: Optional[float]
    swell_period: Optional[float]
    wind_wave_height: Optional[float]
    wind_wave_period: Optional[float]
    swell_direction: Optional[str]
    wind_wave_direction: Optional[str]
    steepness: Optional[str]
    average_wave_period: Optional[float]
    mean_wave_direction: Optional[int]


# Properties to receive on item creation
class WaveDatumCreate(WaveDatumBase):
    ...


# Properties to receive on item update
class WaveDatumUpdate(WaveDatumBase):
    ...


# Properties shared by models stored in DB
class WaveDatumInDBBase(WaveDatumBase):
    id: int

    class Config:
        orm_mode = True


class WaveDatum(WaveDatumInDBBase):
    ...


# Properties properties stored in DB
class WaveDatumInDB(WaveDatumInDBBase):
    ...
