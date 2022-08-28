from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class WaveDataBase(BaseModel):
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
class WaveDataCreate(WaveDataBase):
    ...


# Properties to receive on item update
class WaveDataUpdate(WaveDataBase):
    ...


# Properties shared by models stored in DB
class WaveDataInDBBase(WaveDataBase):
    id: int

    class Config:
        orm_mode = True


class WaveData(WaveDataInDBBase):
    ...


# Properties properties stored in DB
class WaveDataInDB(WaveDataInDBBase):
    ...
