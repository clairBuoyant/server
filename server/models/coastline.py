from geoalchemy2.types import Geography
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from server.db.base_class import Base


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
    buoy = relationship("Buoy", back_populates="coastlines", uselist=False)
