import pytest
from fastapi.testclient import TestClient

from server.main import app, db


@pytest.fixture(scope="module")
def test_app() -> TestClient:
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def db_session(db=db):
    yield db
