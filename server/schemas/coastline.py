from typing import Optional

from geoalchemy2.elements import WKBElement  # type: ignore
from pydantic import BaseModel, validator

from server.schemas.buoy import Buoy
from server.schemas.common import ewkb_to_wkt


# Shared properties
class CoastlineBase(BaseModel):
    geom: str  # Geography(geometry_type="MULTILINE")
    station_id: str


# Properties to receive on item creation
class CoastlineCreate(CoastlineBase):
    ...


# Properties to receive on item update
class CoastlineUpdate(CoastlineBase):
    ...


# Properties shared by models stored in DB
class CoastlineInDBBase(CoastlineBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Coastline(CoastlineInDBBase):
    buoy: Optional[Buoy]

    @validator("geom", pre=True, allow_reuse=True, always=True)
    def correct_geom_format(cls, v):
        if not isinstance(v, WKBElement):
            raise ValueError("Must be a valid WKBE element")
        return ewkb_to_wkt(v)


# Properties properties stored in DB
class CoastlineInDB(CoastlineInDBBase):
    ...
