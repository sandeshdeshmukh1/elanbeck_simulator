from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings
from app.tests.utils.utils import random_email


def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "username": settings.FIRST_SUPERUSER_EMAIL,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/get-access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_use_access_token(
    client: TestClient, superuser_token_headers: Dict[str, str]
) -> None:
    r = client.post(
        f"{settings.API_V1_STR}/login/verify-token", headers=superuser_token_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "email" in result


def test_forgot_email_not_existing_email(
    client: TestClient
) -> None:
    email = random_email()
    r = client.post(
        f"{settings.API_V1_STR}/login/password-recovery/{email}")
    assert r.status_code == 201


def test_forgot_email_existing_email(
    client: TestClient
) -> None:
    email = settings.FIRST_SUPERUSER_EMAIL
    r = client.post(
        f"{settings.API_V1_STR}/login/password-recovery/{email}")
    assert r.status_code == 200