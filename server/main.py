import logging
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Callable

from server.db.session import get_db

database = get_db()


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        logging.info("connecting to a database")
        # await database
        logging.info("Database connection - successful")

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        logging.info("Closing connection to database")
        # await database.disconnect()
        logging.info("Database connection - closed")

    return stop_app


description_markdown = """
clairBuoyant API provides you with timely buoy data from NDBC.

## Buoys

You can **read buoy** data. (_not implemented_).
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
    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    return application


app = get_application()


# @app.on_event("startup")
# async def startup():
#     await db.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await db.disconnect()


@app.get("/api/v1")
def root():
    return {"message": "Hello world!"}


# TODO: add routes

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
