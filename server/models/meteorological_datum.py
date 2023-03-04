from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy.orm import Mapped, relationship

from server.db.base_class import Base, buoy_fk, intpk

if TYPE_CHECKING:
    from server.models.buoy import Buoy


class MeteorologicalDatum(Base):
    __tablename__ = "meteorological_data"

    buoy: Mapped["Buoy"] = relationship(back_populates="meteorological_data")

    id: Mapped[intpk]
    station_id: Mapped[buoy_fk]
    date_recorded: Mapped[datetime]
    wind_direction: Mapped[Optional[int]]
    wind_speed: Mapped[Optional[float]]
    wind_gust: Mapped[Optional[float]]
    wave_height: Mapped[Optional[float]]
    dominant_wave_period: Mapped[Optional[float]]
    average_wave_period: Mapped[Optional[float]]
    wave_direction: Mapped[Optional[int]]
    sea_level_pressure: Mapped[Optional[float]]
    pressure_tendency: Mapped[Optional[float]]
    air_temperature: Mapped[Optional[float]]
    water_temperature: Mapped[Optional[float]]
    dewpoint_temperature: Mapped[Optional[float]]
    visibility: Mapped[Optional[float]]
    tide: Mapped[Optional[float]]
