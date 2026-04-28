import pytest
from utils.api_client import get

@pytest.fixture(scope="session")
def users_response():
    return get("users")

@pytest.fixture(scope="session")
def invalid_response():
    return get("invalid-users")

