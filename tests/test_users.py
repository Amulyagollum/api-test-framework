from utils.api_client import get


def test_get_users_status_code(users_response):
    assert users_response.status_code == 200


def test_invalid_users_status_code(invalid_response):
    assert invalid_response.status_code == 404   # also fix this (see below)


def test_users_response_structure(users_response):
    data = users_response.json()

    assert isinstance(data, list)
    assert "id" in data[0]
    assert "email" in data[0]