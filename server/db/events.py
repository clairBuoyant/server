"""PURPOSE: https://fastapi.tiangolo.com/advanced/events/

TODO: https://docs.sqlalchemy.org/en/14/core/connections.html
    * Investigate whether there are any significant advantages with managing connections ourselves.
    * Alternative: use `get_db` with Dependency hook for every API request.
"""
import logging

import asyncpg
from fastapi import FastAPI

from server.core.config import Settings


async def connect_to_db(app: FastAPI, settings: Settings) -> None:
    logging.info("Connecting to PostgreSQL")

    app.state.pool = await asyncpg.create_pool(
        str(settings.DATABASE_URL),
        min_size=settings.min_connection_count,  # ! not implemented
        max_size=settings.max_connection_count,  # ! not implemented
    )

    logging.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logging.info("Closing connection to database")

    await app.state.pool.close()

    logging.info("Connection closed")
