from typing import List

import dataset
import pytest
from dataset.types import Types

from app.modules.posts.adapters.repository import DatasetPostRepository
from app.modules.posts.domain.model import Post
from tests.unit.posts.conftest import get_fake_post, get_fake_posts


def get_database():
    database = dataset.Database("sqlite://")
    database.create_table("post", primary_id="id", primary_type=Types.string)
    return database


def get_initial_posts() -> List[Post]:
    return get_fake_posts()


def add_init_posts(database: dataset.Database) -> List[Post]:
    posts = get_fake_posts()
    with database as tx:
        table = tx.get_table("post")
        table.insert_many([post.dict() for post in posts])
    return posts


def test_find_all():
    # given
    database = get_database()
    initial_posts = add_init_posts(database)
    post_repository = DatasetPostRepository(db=database)

    # when
    posts = post_repository.find_all()

    # then
    assert posts == initial_posts


def test_find_by_id():
    # given
    database = get_database()
    initial_posts = add_init_posts(database)
    post_repository = DatasetPostRepository(db=database)
    id = initial_posts[0].id

    # when
    post = post_repository.find_by_id(id)

    # then
    assert post == initial_posts[0]


def test_save():
    # given
    database = get_database()
    post_repository = DatasetPostRepository(db=database)
    post = get_fake_post()

    # when
    post_repository.save(post)
    post.title = "updated name"
    post_repository.save(post)

    # then
    assert post_repository.find_all() == [post]


def test_delete_by_id():
    # given
    database = get_database()
    posts = add_init_posts(database)
    post_repository = DatasetPostRepository(db=database)

    # when
    post_repository.delete_by_id(posts[0].id)

    # then
    assert post_repository.find_all() == posts[1:]


if __name__ == "__main__":
    pytest.main(".")
