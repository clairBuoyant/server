from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from server.core.config import get_settings
from server.db.base_class import Base


class Database:
    def __init__(self, connection_url: str):
        self.db_url = connection_url
        self._engine: AsyncEngine = None
        self._session: AsyncSession = None

    async def create_all(self):  # pragma: no cover
        async with self._engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    def __getattr__(self, name) -> AsyncSession:
        return getattr(self._session, name)

    async def init(self):
        # closes connections if a session is created,
        # so as not to create repeated connections.
        if self._session:
            await self._session.close()
        self._engine = create_async_engine(self.db_url, echo=True, future=True)
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()


settings = get_settings()
db = Database(settings.DATABASE_URL)
