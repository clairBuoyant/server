from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ForecastBase(BaseModel):
    date_recorded: datetime
    station_id: str
    wave_height: Optional[float]
    wind_direction: Optional[int]
    wind_speed: Optional[float]
    wind_speed_gust: Optional[float]


# Properties to receive on item creation
class ForecastCreate(ForecastBase):
    ...


# Properties to receive on item update
class ForecastUpdate(ForecastBase):
    ...


# Properties shared by models stored in DB
class ForecastInDBBase(ForecastBase):
    id: int

    class Config:
        orm_mode = True


class Forecast(ForecastInDBBase):
    ...


# Properties properties stored in DB
class ForecastInDB(ForecastInDBBase):
    # TODO: add relationship refs
    ...
