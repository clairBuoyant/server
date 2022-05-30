from typing import Optional

from geoalchemy2.elements import WKBElement
from pydantic import BaseModel, validator

from .common import ewkb_to_wkt

# Shared properties
class BuoyBase(BaseModel):
    station_id: str
    name: str
    owner: str
    location: str  # Geography(geometry_type="POINT")
    elev: Optional[float] = 0.0  # elevation
    pgm: str
    type: str
    met: Optional[str] = "n"
    currents: Optional[str] = "n"
    waterquality: Optional[str] = "n"
    dart: Optional[str] = "n"
    seq: Optional[int] = None  # tao_seq

    @validator("location", pre=True, allow_reuse=True, whole=True, always=True)
    def correct_location_format(cls, v):
        if not isinstance(v, WKBElement):
            raise ValueError("Must be a valid WKBE element")
        return ewkb_to_wkt(v)


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
    ...


# Properties properties stored in DB
class BuoyInDB(BuoyInDBBase):
    ...
