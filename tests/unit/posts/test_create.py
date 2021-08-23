from app.posts.service_layer.create import (
    CreatePost,
    CreatePostRequest,
    CreatePostResponse,
)
from tests.unit.posts.fake_repository import FakePostRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_create_post():
    # given
    uow = FakeUnitOfWork()
    post_repository = FakePostRepository()
    service = CreatePost(post_repository, uow)
    req = CreatePostRequest(title="title", content="content", user_id="hardy")

    # when
    res = service.execute(req)

    # then
    assert res == CreatePostResponse(
        id=res.id, title="title", content="content", user_id="hardy"
    )
