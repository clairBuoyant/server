from typing import Any, Optional

from pydantic import BaseModel


# TODO: fix typing to streamline API validation/serialization
# Shared properties
class BuoyBase(BaseModel):
    station_id: str
    name: str
    owner: str
    location: Any  # Geography(geometry_type="POINT")
    elev: Optional[float] = 0.0  # elevation
    pgm: str
    type: str
    met: Optional[str] = "n"
    currents: Optional[str] = "n"
    waterquality: Optional[str] = "n"
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
    ...


# Properties properties stored in DB
class BuoyInDB(BuoyInDBBase):
    ...
