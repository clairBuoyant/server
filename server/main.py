import uvicorn

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from server import models, schemas

from server.db.session import get_db


description_markdown = """
clairBuoyant API provides you with timely buoy data from NDBC.

## Buoys

You can **read buoy** data. (_not implemented_).

## Coastlines

You can **get coastlines** data.
"""


def get_application() -> FastAPI:
    application = FastAPI(
        description=description_markdown,
        docs_url="/api/v1/docs",
        openapi_url="/api/v1/openapi.json",
        redoc_url=None,
        title="clairBuoyant",
        version="0.1.0",
    )

    # TODO: Specify specific hosts and adjust method/header permissions
    origins = ["localhost"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()

# TODO: move to API folder
@app.get("/api/v1/coastlines")
async def get_coastlines(
    db_session: AsyncSession = Depends(get_db),
) -> models.Coastline:

    # `selectinload`: alternative approach to `joinedload`
    stmt = (
        select(models.Coastline)
        .options(joinedload(models.Coastline.buoy, innerjoin=True))
        .order_by(models.Coastline.id)
    )
    response = await db_session.execute(stmt)

    """TODO
    * Finish schema typing to support validation/serialization

    * Add error handling
    """
    return [schemas.Coastline.from_orm(row.Coastline).dict() for row in response]


@app.get("/api/v1")
def root():
    return {"message": "Hello world!"}


# TODO: add routes

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
