import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine

from server.core.config import get_settings
from server.db.init_db import init_db


settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init() -> None:
    await init_db(engine)


async def async_main() -> None:
    logger.info("Creating initial data")
    await init()
    logger.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(async_main())