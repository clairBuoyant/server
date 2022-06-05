import asyncio
import logging

from server.db.init_db import init_db
from server.db.session import AsyncSessionLocal

# TODO: minimize DB query logs in CI/CD
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


db_session = AsyncSessionLocal


async def init() -> None:
    await init_db(db_session)
    await db_session.close()


async def async_main() -> None:
    logger.info("Creating initial data")
    await init()
    logger.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(async_main())
