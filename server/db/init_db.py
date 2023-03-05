from sqlalchemy.ext.asyncio import AsyncSession

# Make sure all SQL Alchemy models are imported before initializing DB
# https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
from server.db import base  # noqa: F401
from server.db.seeds import (
    seed_active_buoys,
    seed_coastlines,
    seed_forecast_data,
    seed_meteorological_data,
    seed_wave_data,
)


async def init_db(db_session: AsyncSession) -> None:
    await seed_active_buoys(db_session)
    await seed_coastlines(db_session)
    await seed_forecast_data(db_session)
    await seed_meteorological_data(db_session)
    await seed_wave_data(db_session)
