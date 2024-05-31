from fastapi.testclient import TestClient
from sqlalchemy.orm import Session  # type: ignore

from app.core.config import settings
from app.tests.utils.todo import create_random_todo


def test_create_todo(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo"}
    response = client.post(
        f"{settings.API_V1_STR}/todos/create-todo", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert "id" in content
    assert "owner_id" in content


def test_read_todos(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/todos/get-my-todos", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert "total" in content
    assert "size" in content
    assert "page" in content
