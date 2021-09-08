from app.modules.posts.service_layer.use_cases.delete import (
    DeletePost,
    DeletePostRequest,
)
from tests.unit.posts.conftest import get_fake_posts
from tests.unit.posts.fake_repository import FakePostRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_delete_post():
    # given
    uow = FakeUnitOfWork()
    posts = get_fake_posts()
    post_repository = FakePostRepository(posts=posts)
    service = DeletePost(post_repository, uow)
    req = DeletePostRequest(id=str(posts[0].id), requested_user_id=posts[0].user_id)

    # when
    service.execute(req)

    # then
    print(posts)
    assert len(post_repository.find_all()) == len(posts[1:])
