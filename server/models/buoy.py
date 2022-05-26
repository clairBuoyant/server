from geoalchemy2.types import Geography
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, SmallInteger, String

from server.db.base_class import Base


class Buoy(Base):
    __tablename__ = "buoys"

    id = Column(Integer, index=True, nullable=False, primary_key=True)
    station_id = Column(String(10), index=True, nullable=False, unique=True)
    name = Column(String(200), nullable=False)
    owner = Column(String(200), nullable=False)
    location = Column(
        Geography(geometry_type="POINT", nullable=False, srid=4326, spatial_index=True)
    )
    elev = Column(Float(precision=10), default=0.0, nullable=False)  # elevation
    pgm = Column(String(50), nullable=False)
    type = Column(String(10), nullable=False)
    met = Column(String(1), default="n", nullable=False)
    currents = Column(String(1), default="n", nullable=False)
    water_quality = Column(String(1), default="n", nullable=False)
    dart = Column(String(1), default="n", nullable=False)
    seq = Column(SmallInteger, nullable=True)  # tao_seq

    coastlines = relationship("Coastline", back_populates="buoy", uselist=True)
