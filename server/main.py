import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.api.v1.endpoints import coastlines

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
app.include_router(coastlines.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
