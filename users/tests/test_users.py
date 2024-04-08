from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
def test_if_user_is_anonymous_return_401():
    client = APIClient()
    response = client.get(
        '/auth/users/referral/')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED  # type: ignore


@pytest.mark.django_db
def test_data_creation():
    client = APIClient()
    response = client.post(
        "/auth/users/", {"email": "a", "username": "a", "password": "a", })

    assert response.status_code == status.HTTP_201_CREATED  # type: ignore
