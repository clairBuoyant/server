import inspect

import pytest
from fastapi.testclient import TestClient

from server.main import app


# Dynamically adds asyncio marker
def pytest_collection_modifyitems(config, items):  # noqa
    for item in items:
        if inspect.iscoroutinefunction(item.function):
            item.add_marker(pytest.mark.asyncio)


# TODO: override app settings with test env
# def get_settings_override():
#     return Settings(
#         DATABASE_URL="connection_string_to_psql",
#         PYTHON_ENV="test",
#     )

# TODO: abstract db connection without needing to access private attributes or close sessions repetitively
# @pytest.fixture(scope="session")
# def get_test_db(db=db):
#     yield db


@pytest.fixture(scope="module")
def test_app() -> TestClient:
    with TestClient(app) as client:
        yield client
