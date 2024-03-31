from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# Shared properties
class ForecastBase(BaseModel):
    date_recorded: datetime
    station_id: str
    wave_height: Optional[float] = None
    wind_direction: Optional[int] = None
    wind_speed: Optional[float] = None
    wind_speed_gust: Optional[float] = None


# Properties to receive on item creation
class ForecastCreate(ForecastBase): ...


# Properties to receive on item update
class ForecastUpdate(ForecastBase): ...


# Properties shared by models stored in DB
class ForecastInDBBase(ForecastBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class Forecast(ForecastInDBBase): ...


# Properties properties stored in DB
class ForecastInDB(ForecastInDBBase):
    # TODO: add relationship refs
    ...
