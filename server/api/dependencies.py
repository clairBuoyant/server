from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server.db.database import db


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    try:
        yield db._session
    finally:
        await db.close()


CurrentAsyncDBSession = Annotated[AsyncSession, Depends(get_db)]
