from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from server.db.database import db


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    try:
        yield db._session
    finally:
        await db.close()
