from app.modules.posts.service_layer.use_cases.update import (
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
    req = UpdatePostRequest(
        id=post.id,
        title="modified title",
        content=post.content,
        requested_user_id=post.user_id,
    )

    # when
    res = service.execute(req)

    # then
    assert res == UpdatePostResponse(
        id=post.id, title="modified title", content=post.content, user_id=post.user_id
    )
    assert post_repository.find_by_id(str(post.id)).title == "modified title"
