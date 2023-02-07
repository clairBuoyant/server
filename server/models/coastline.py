from typing import TYPE_CHECKING, Optional

from geoalchemy2.types import Geography  # type: ignore
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.db.base_class import Base, buoy_fk, intpk

if TYPE_CHECKING:
    from server.models.buoy import Buoy


class Coastline(Base):
    __tablename__ = "coastlines"

    # TODO: revisit relationship strategy to avoid N+1 scenarios
    buoy: Mapped[Optional["Buoy"]] = relationship(
        "Buoy", back_populates="coastlines", lazy="joined"
    )

    id: Mapped[intpk]
    station_id: Mapped[buoy_fk]
    geom: Mapped[Geography] = mapped_column(
        Geography(
            geometry_type="GEOMETRY", nullable=False, srid=4326, spatial_index=True
        )
    )
