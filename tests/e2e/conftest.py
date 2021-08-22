import pytest


@pytest.fixture
def server_url() -> str:
    return "127.0.0.1:8000"
