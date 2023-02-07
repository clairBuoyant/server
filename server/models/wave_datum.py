from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy.orm import Mapped, relationship

from server.db.base_class import Base, buoy_fk, intpk

if TYPE_CHECKING:
    from server.models.buoy import Buoy


class WaveDatum(Base):
    __tablename__ = "wave_data"

    buoy: Mapped["Buoy"] = relationship("Buoy", back_populates="wave_data")

    id: Mapped[intpk]
    station_id: Mapped[buoy_fk]
    date_recorded: Mapped[datetime]
    significant_wave_height: Mapped[Optional[float]]
    swell_height: Mapped[Optional[float]]
    swell_period: Mapped[Optional[float]]
    wind_wave_height: Mapped[Optional[float]]
    wind_wave_period: Mapped[Optional[float]]
    swell_direction: Mapped[Optional[str]]
    wind_wave_direction: Mapped[Optional[str]]
    steepness: Mapped[Optional[str]]
    average_wave_period: Mapped[Optional[float]]
    mean_wave_direction: Mapped[Optional[int]]
