from typing import List

import dataset
import pytest
from dataset.types import Types

from app.modules.users.adapters.repository import DatasetUserRepository
from app.modules.users.domain.model import User
from tests.unit.users.conftest import get_fake_user, get_fake_users


def get_database():
    database = dataset.Database("sqlite://")
    database.create_table("user", primary_id="id", primary_type=Types.string)
    return database


def get_initial_users() -> List[User]:
    return get_fake_users()


def add_init_users(database: dataset.Database) -> List[User]:
    users = get_fake_users()
    with database as tx:
        table = tx.get_table("user")
        table.insert_many([user.dict() for user in users])
    return users


def test_find_all():
    # given
    database = get_database()
    add_init_users(database)
    user_repository = DatasetUserRepository(db=database)

    # when
    users = user_repository.find_all()

    # then
    assert users == get_initial_users()


def test_find_by_id():
    # given
    database = get_database()
    add_init_users(database)
    user_repository = DatasetUserRepository(db=database)
    id = get_initial_users()[0].id

    # when
    user = user_repository.find_by_id(id)

    # then
    assert user == get_initial_users()[0]


def test_save():
    # given
    database = get_database()
    user_repository = DatasetUserRepository(db=database)
    user = get_fake_user()

    # when
    user_repository.save(user)
    user.name = "updated name"
    user_repository.save(user)

    # then
    assert user_repository.find_all() == [user]


def test_delete_by_id():
    # given
    database = get_database()
    users = add_init_users(database)
    user_repository = DatasetUserRepository(db=database)

    # when
    user_repository.delete_by_id(users[0].id)

    # then
    assert user_repository.find_all() == users[1:]


if __name__ == "__main__":
    pytest.main(".")
