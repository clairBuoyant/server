from sqlalchemy.orm import Session

# from src.db import crud, schemas
from services.buoy.scrape_buoy import NDBCScraper_Buoy

# from src.core.config import settings
from server.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


async def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # if you don't want to use migrations,
    # uncomment the next line to create all tables
    # Base.metadata.create_all(bind=engine)
    await NDBCScraper_Buoy(db)
