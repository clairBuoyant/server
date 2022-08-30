from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

# Make sure all SQL Alchemy models are imported before initializing DB
# https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
from server.db import base  # noqa: F401
from server.services.buoy.seed_buoys import seed_active_buoys
from server.services.coastline.seed_coastline import seed_rockaway
from server.services.meteorological_datum.seed_meteorological_datum import (
    seed_meteorological_data,
)
from server.services.wave_datum.seed_wave_datum import seed_wave_datum


async def init_db(db_session: AsyncSession) -> None:
    await seed_active_buoys(db_session)
    await seed_rockaway(db_session)
    await seed_meteorological_data(db_session)
    await seed_wave_datum(db_session)
