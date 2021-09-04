from app.modules.posts.service_layer.use_cases.read import (
    ReadPost,
    ReadPostRequest,
    ReadPostResponse,
    ReadPosts,
    ReadPostsRequest,
    ReadPostsResponse,
)
from tests.unit.posts.conftest import get_fake_posts
from tests.unit.posts.fake_repository import FakePostRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_read_posts():
    # given
    uow = FakeUnitOfWork()
    posts = get_fake_posts()
    post_repository = FakePostRepository(posts=posts)
    service = ReadPosts(post_repository, uow)
    req = ReadPostsRequest()

    # when
    res = service.execute(req)

    # then
    assert res == ReadPostsResponse(
        items=[ReadPostResponse(**post.dict()) for post in posts]
    )


def test_read_posts_by_user_id():
    # given
    uow = FakeUnitOfWork()
    posts = get_fake_posts()
    post = posts[0]
    post_repository = FakePostRepository(posts=posts)
    service = ReadPosts(post_repository, uow)
    req = ReadPostsRequest(user_id=post.user_id)

    # when
    res = service.execute(req)

    # then
    assert res == ReadPostsResponse(items=[ReadPostResponse(**post.dict())])


def test_read_post():
    # given
    uow = FakeUnitOfWork()
    posts = get_fake_posts()
    post = posts[0]
    post_repository = FakePostRepository(posts=posts)
    service = ReadPost(post_repository, uow)
    req = ReadPostRequest(id=str(post.id))

    # when
    res = service.execute(req)

    # then
    assert res == ReadPostResponse(**post.dict())
