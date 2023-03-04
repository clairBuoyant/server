from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing_extensions import Annotated

str1 = Annotated[str, 1]
str10 = Annotated[str, 10]

# set up mapped_column() overrides to be used in multiple files
intpk = Annotated[int, mapped_column(index=True, nullable=False, primary_key=True)]
buoy_fk = Annotated[str10, mapped_column(ForeignKey("buoys.station_id"))]
buoyattr_sint = Annotated[int, mapped_column(SmallInteger, nullable=True)]
buoyattr_str1 = Annotated[str, mapped_column(String(1), default="n", nullable=False)]


# TODO: consider incorporating `MappedAsDataclass` to Base.
class Base(DeclarativeBase):
    type_annotation_map = {
        str1: String(1),
        str10: String(10),
    }
