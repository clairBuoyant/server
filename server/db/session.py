import logging
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from server.core.config import get_settings

settings = get_settings()

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = AsyncSession(
    autocommit=False, autoflush=False, bind=engine, future=True
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    db = AsyncSessionLocal
    try:
        logging.info("connecting to a database")
        yield db
        logging.info("Database connection - successful")
    finally:
        logging.info("Closing connection to database")
        # TODO: investigate: INFO sqlalchemy.engine.Engine ROLLBACK
        await db.close()
        logging.info("Database connection - closed")
