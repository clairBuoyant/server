from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from server.core.config import Settings


class Database:
    def __init__(self, connection_url):
        self._session = None
        self._engine = None
        self.url = connection_url

    async def create_all(self):  # pragma: no cover
        Base = declarative_base()
        async with self._engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    def __getattr__(self, name) -> AsyncSession:
        return getattr(self._session, name)

    async def init(self, is_test=False):
        # closes connections if a session is created,
        # so as not to create repeated connections
        if self._session:
            await self._session.close()
        db_url = self.url + "_test" if is_test else self.url  # TODO: refactor
        self._engine = create_async_engine(db_url, echo=True, future=True)
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()


settings = Settings()
# TODO: dynamically append '_test' based on PYTHON_ENV
db: AsyncSession | Database = Database(settings.DATABASE_URL)
