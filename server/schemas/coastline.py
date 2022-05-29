from typing import Any, Optional

from pydantic import BaseModel

from .buoy import Buoy


# Shared properties
class CoastlineBase(BaseModel):
    # TODO: fix typing to streamline API validation/serialization
    geom: Any  # Geography(geometry_type="MULTILINE")
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
    # TODO: fix typing to streamline API validation/serialization
    buoy: Optional[Buoy]


# Properties properties stored in DB
class CoastlineInDB(CoastlineInDBBase):
    ...
