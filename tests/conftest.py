import inspect
import os
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# if __name__ == "__main__" and server folder is not on PYTHONPATH
server_fpath = str(Path(os.path.join(os.path.dirname(__file__))).parent)
if server_fpath not in sys.path:
    sys.path.append(server_fpath)


from server.main import app  # noqa: E402


# Dynamically adds asyncio marker
def pytest_collection_modifyitems(config, items):  # noqa
    for item in items:
        if inspect.iscoroutinefunction(item.function):
            item.add_marker(pytest.mark.asyncio)


@pytest.fixture(scope="module")
def test_app() -> TestClient:
    with TestClient(app) as client:
        yield client
