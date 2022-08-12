from typing import Optional

from geoalchemy2.elements import WKBElement  # type: ignore
from pydantic import BaseModel, validator

from server.schemas.common import ewkb_to_coords


# Shared properties
class BuoyBase(BaseModel):
    station_id: str
    name: str
    owner: str
    location: tuple[float, float] | str  # [lon, lat] or POINT(lon lat)
    elev: Optional[float] = 0.0  # elevation
    pgm: str
    type: str
    met: Optional[str] = "n"
    currents: Optional[str] = "n"
    water_quality: Optional[str] = "n"
    dart: Optional[str] = "n"
    seq: Optional[int] = None  # tao_seq


# Properties to receive on item creation
class BuoyCreate(BuoyBase):
    ...


# Properties to receive on item update
class BuoyUpdate(BuoyBase):
    ...


# Properties shared by models stored in DB
class BuoyInDBBase(BuoyBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Buoy(BuoyInDBBase):
    @validator("location", pre=True, allow_reuse=True, always=True)
    def correct_location_format(cls, v):
        if not isinstance(v, WKBElement):
            raise ValueError("Must be a valid WKBE element")
        return ewkb_to_coords(v)


# Properties properties stored in DB
class BuoyInDB(BuoyInDBBase):
    ...
