from app.posts.service_layer.update import (
    UpdatePost,
    UpdatePostRequest,
    UpdatePostResponse,
)
from tests.unit.posts.conftest import get_fake_posts
from tests.unit.posts.fake_repository import FakePostRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_update_post():
    # given
    uow = FakeUnitOfWork()
    posts = get_fake_posts()
    post_repository = FakePostRepository(posts=posts)
    service = UpdatePost(post_repository, uow)
    post = posts[0]
    post.title = "modified title"
    req = UpdatePostRequest(**post.dict())

    # when
    res = service.execute(req)

    # then
    assert res == UpdatePostResponse(**post.dict())
    assert post_repository.find_by_id(str(post.id)) == post
