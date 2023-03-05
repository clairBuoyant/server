from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy.orm import Mapped, relationship

from server.db.base_class import Base, buoy_fk, intpk

if TYPE_CHECKING:
    from server.models.buoy import Buoy


class Forecast(Base):
    __tablename__ = "forecasts"

    buoy: Mapped["Buoy"] = relationship(back_populates="forecasts")

    id: Mapped[intpk]
    # TODO: consider renaming
    date_recorded: Mapped[datetime]  # prediction date
    station_id: Mapped[buoy_fk]
    wave_height: Mapped[Optional[float]]
    wind_direction: Mapped[Optional[int]]
    wind_speed: Mapped[Optional[float]]
    wind_speed_gust: Mapped[Optional[float]]
