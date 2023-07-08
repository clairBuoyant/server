from typing import Optional

from geoalchemy2.elements import WKBElement  # type: ignore
from pydantic import BaseModel, ConfigDict, validator

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
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Coastline(CoastlineInDBBase):
    buoy: Optional[Buoy] = None

    # TODO: replace `validator` with `field_validator`
    # https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators
    @validator("geom", pre=True, allow_reuse=True, always=True)
    def correct_geom_format(cls, v):
        if not isinstance(v, WKBElement):
            raise ValueError("Must be a valid WKBE element")
        return ewkb_to_wkt(v)


# Properties properties stored in DB
class CoastlineInDB(CoastlineInDBBase):
    ...
