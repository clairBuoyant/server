from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

from server.db.base_class import Base
from server.models.buoy import Buoy


class WaveData(Base):
    __tablename__ = "wave_data"

    id = Column(Integer, index=True, nullable=False, primary_key=True)
    station_id = Column(
        String(10),
        ForeignKey(Buoy.station_id),
        index=True,
        nullable=False,
        unique=False,
    )
    date_recorded = Column(DateTime, nullable=False)
    wave_height = Column(Float, nullable=True)
    swell_height = Column(Float, nullable=True)
    swell_period = Column(Float, nullable=True)
    wind_wave_height = Column(Float, nullable=True)
    wind_wave_period = Column(Float, nullable=True)
    swell_direction = Column(String, nullable=True)
    wind_wave_direction = Column(String, nullable=True)
    steepness = Column(String, nullable=True)
    average_wave_period = Column(Float, nullable=True)
