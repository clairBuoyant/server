from typing import TYPE_CHECKING, Optional

from geoalchemy2.types import Geography
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from server.db.base_class import Base

if TYPE_CHECKING:
    from .buoy import Buoy


class Coastline(Base):
    __tablename__ = "coastlines"

    id = Column(Integer, index=True, nullable=False, primary_key=True)
    station_id = Column(
        String(10),
        ForeignKey("buoys.station_id"),
        index=True,
        nullable=False,
        unique=True,
    )
    geom = Column(
        Geography(
            geometry_type="GEOMETRY", nullable=False, srid=4326, spatial_index=True
        )
    )
    # TODO: revisit relationship strategy to avoid N+1 problem
    buoy: Optional["Buoy"] = relationship("Buoy", backref="coastlines", lazy="joined")
