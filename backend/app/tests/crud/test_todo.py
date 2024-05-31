from sqlalchemy.orm import Session  # type: ignore

from app import crud
from app.schemas.todo import TodoCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_todo(db: Session) -> None:
    title = random_lower_string()
    todo_in = TodoCreate(title=title)
    user = create_random_user(db)
    todo = crud.todo.create_with_owner(db=db, obj_in=todo_in, owner_id=user.id)
    assert todo.title == title
    assert todo.owner_id == user.id


def test_get_todo(db: Session) -> None:
    title = random_lower_string()
    todo_in = TodoCreate(title=title)
    user = create_random_user(db)
    todo = crud.todo.create_with_owner(db=db, obj_in=todo_in, owner_id=user.id)
    stored_todo = crud.todo.get(db=db, id=todo.id)
    assert stored_todo
    assert todo.id == stored_todo.id
    assert todo.title == stored_todo.title
    assert todo.owner_id == stored_todo.owner_id


def test_delete_todo(db: Session) -> None:
    title = random_lower_string()
    todo_in = TodoCreate(title=title)
    user = create_random_user(db)
    todo = crud.todo.create_with_owner(db=db, obj_in=todo_in, owner_id=user.id)
    todo2 = crud.todo.remove(db=db, id=todo.id)
    todo3 = crud.todo.get(db=db, id=todo.id)
    assert todo3 is None
    assert todo2.id == todo.id
    assert todo2.title == title
    assert todo2.owner_id == user.id
