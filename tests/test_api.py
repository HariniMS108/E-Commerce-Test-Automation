from api.api_client import APIClient


def test_get_post():

    api = APIClient()

    response = api.get_post(1)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1


def test_create_post():

    api = APIClient()

    response = api.create_post(
        "Test Product",
        "This is a test product",
        1
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Test Product"
    assert data["body"] == "This is a test product"
    assert data["userId"] == 1