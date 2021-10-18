import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    application = FastAPI(
        title="clairBuoyant", version="0.1.0", docs_url="/api/docs", openapi_url="/api"
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


@app.get("/api/v1")
async def root():
    return {"message": "Hello world!"}


# TODO: add routes

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
