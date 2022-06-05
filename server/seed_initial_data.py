import asyncio
import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from server.core.config import get_settings
from server.db.init_db import init_db

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


settings = get_settings()

engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)

db_session = AsyncSession(autocommit=False, autoflush=False, bind=engine, future=True)


async def init() -> None:  # pragma: no cover
    await init_db(db_session)
    await db_session.close()


async def async_main() -> None:  # pragma: no cover
    logger.info("Creating initial data")
    await init()
    logger.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(async_main())
