import os
import sys
from pathlib import Path

# TODO: consolidate duplication of this block of code (seed_initial_data and conftest)
# if __name__ == "__main__" and server folder is not on PYTHONPATH
server_fpath = str(Path(os.path.join(os.path.dirname(__file__))).parent)
if server_fpath not in sys.path:
    sys.path.append(server_fpath)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.api.v1.api import api_router
from server.core.constants import API_PREFIX
from server.db.database import db

description_markdown = """
clairBuoyant API provides you with timely buoy data from NDBC.

## Buoys

You can **get buoys** data.

You can **get buoy** data by `station_id`.

## Coastlines

You can **get coastlines** data.

You can **get coastline** by `coastline_id`.
"""


def get_application() -> FastAPI:
    application = FastAPI(
        description=description_markdown,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        redoc_url=None,
        title="clairBuoyant",
        version="0.1.1",
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


@app.on_event("startup")
async def startup_event():
    await db.init()
    await db.create_all()


@app.on_event("shutdown")
async def shutdown_event():
    await db.close()


app.include_router(api_router, prefix=API_PREFIX)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
