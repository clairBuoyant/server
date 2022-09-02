from sqlalchemy import (  # type: ignore
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)

from server.db.base_class import Base
from server.models.buoy import Buoy


class MeteorologicalDatum(Base):
    __tablename__ = "meteorological_data"

    id = Column(Integer, index=True, nullable=False, primary_key=True)
    station_id = Column(
        String(10),
        ForeignKey(Buoy.station_id),
        index=True,
        nullable=False,
        unique=False,
    )
    date_recorded = Column(DateTime, nullable=False)
    wind_direction = Column(Integer, nullable=True)
    wind_speed = Column(Float, nullable=True)
    wind_gust = Column(Float, nullable=True)
    wave_height = Column(Float, nullable=True)
    dominant_wave_period = Column(Float, nullable=True)
    average_wave_period = Column(Float, nullable=True)
    wave_direction = Column(Integer, nullable=True)
    sea_level_pressure = Column(Float, nullable=True)
    pressure_tendency = Column(Float, nullable=True)
    air_temperature = Column(Float, nullable=True)
    water_temperature = Column(Float, nullable=True)
    dewpoint_temperature = Column(Float, nullable=True)
    visibility = Column(Float, nullable=True)
    tide = Column(Float, nullable=True)
