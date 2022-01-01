from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from server.core.config import get_settings


settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL,
)

AsyncSessionLocal = AsyncSession(
    autocommit=False, autoflush=False, bind=engine, future=True
)

Base = declarative_base()


def get_db():
    async def run():
        db: AsyncSession = AsyncSessionLocal()
        try:
            yield db
        finally:
            await db.close()

    return run
