# Import all the models, so that Base has them before being
# imported by Alembic
from server.db.base_class import Base  # noqa: F401
from server.models.buoy import Buoy  # noqa: F401
from server.models.coastline import Coastline  # noqa: F401
