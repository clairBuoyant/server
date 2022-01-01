from typing import Any, Optional

# from geoalchemy2.types import Geography
from pydantic import BaseModel


# TODO: refactor into smaller models for read/write types
class BuoyBase(BaseModel):
    station_id: str
    name: str
    owner: str
    location: Any  # TODO: finish type implementation for Geography(geometry_type="POINT")
    elev: Optional[float] = 0.0  # elevation
    pgm: str
    buoy_type: str
    met: Optional[str] = "n"
    currents: Optional[str] = "n"
    waterquality: Optional[str] = "n"
    dart: Optional[str] = "n"
    seq: Optional[int] = None  # tao_seq


class BuoyCreate(BuoyBase):
    ...


class Buoy(BuoyBase):
    id: int

    class Config:
        orm_mode = True
