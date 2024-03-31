from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# Shared properties
class WaveDatumBase(BaseModel):
    station_id: str
    date_recorded: datetime
    significant_wave_height: Optional[float] = None
    swell_height: Optional[float] = None
    swell_period: Optional[float] = None
    wind_wave_height: Optional[float] = None
    wind_wave_period: Optional[float] = None
    swell_direction: Optional[str] = None
    wind_wave_direction: Optional[str] = None
    steepness: Optional[str] = None
    average_wave_period: Optional[float] = None
    mean_wave_direction: Optional[int] = None


# Properties to receive on item creation
class WaveDatumCreate(WaveDatumBase): ...


# Properties to receive on item update
class WaveDatumUpdate(WaveDatumBase): ...


# Properties shared by models stored in DB
class WaveDatumInDBBase(WaveDatumBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class WaveDatum(WaveDatumInDBBase): ...


# Properties properties stored in DB
class WaveDatumInDB(WaveDatumInDBBase): ...
