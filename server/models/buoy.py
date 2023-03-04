from typing import TYPE_CHECKING, List, Optional

from geoalchemy2.types import Geography  # type: ignore
from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.db.base_class import Base, buoyattr_sint, buoyattr_str1, intpk, str10

if TYPE_CHECKING:
    from server.models.coastline import Coastline
    from server.models.meteorological_datum import MeteorologicalDatum
    from server.models.wave_datum import WaveDatum


class Buoy(Base):
    __tablename__ = "buoys"

    coastlines: Mapped[List["Coastline"]] = relationship()
    meteorological_data: Mapped[List["MeteorologicalDatum"]] = relationship()
    wave_data: Mapped[List["WaveDatum"]] = relationship()

    id: Mapped[intpk]
    station_id: Mapped[str] = mapped_column(
        String(10), index=True, nullable=False, unique=True
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    owner: Mapped[str] = mapped_column(String(200), nullable=False)
    location: Mapped[Geography] = mapped_column(
        Geography(geometry_type="POINT", nullable=False, srid=4326, spatial_index=True)
    )
    pgm: Mapped[str] = mapped_column(String(50), nullable=False)
    type: Mapped[str10]
    seq: Mapped[Optional[buoyattr_sint]]  # tao_seq

    elev: Mapped[float] = mapped_column(
        Float(precision=10), default=0.0, nullable=False
    )
    met: Mapped[buoyattr_str1]
    currents: Mapped[buoyattr_str1]
    water_quality: Mapped[buoyattr_str1]
    dart: Mapped[buoyattr_str1]
