import pytest
from fastapi.testclient import TestClient

from server.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client
