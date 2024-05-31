from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session  # type: ignore

from app import crud
from app.core.config import settings
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def test_signup_new_user(client: TestClient, db: Session) -> None:
    email = random_email()
    first_name = random_lower_string()
    last_name = random_lower_string()
    password = random_lower_string()
    data = {
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    }
    r = client.post(
        f"{settings.API_V1_STR}/users/signup", json=data,
    )

    assert r.status_code == 200
    user = crud.user.get_by_email(db, email=email)
    assert user
    assert user.email == email
    assert user.first_name == first_name
    assert user.last_name == last_name


def test_signup_existing_user(client: TestClient, db: Session) -> None:
    email = random_email()
    first_name = random_lower_string()
    last_name = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    user = crud.user.create(db, obj_in=user_in)
    data = {
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    }
    r = client.post(
        f"{settings.API_V1_STR}/users/signup", json=data,
    )
    assert r.status_code == 400


def test_get_user_info(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    email = settings.FIRST_SUPERUSER_EMAIL
    first_name = settings.FIRST_SUPERUSER_FIRST_NAME
    last_name = settings.FIRST_SUPERUSER_LAST_NAME
    r = client.get(
        f"{settings.API_V1_STR}/users/get-my-info", headers=superuser_token_headers,
    )
    api_user = r.json()
    assert r.status_code == 200
    assert api_user["email"] == email
    assert api_user["first_name"] == first_name
    assert api_user["last_name"] == last_name
