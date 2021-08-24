from app.users.service_layer.authorize import (
    AuthorizeUser,
    AuthorizeUserRequest,
    AuthorizeUserResponse,
)
from tests.unit.users.conftest import get_fake_users
from tests.unit.users.fake_repository import FakeUserRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_authorzie_user():
    # given
    users = get_fake_users()
    user = users[0]
    user_repository = FakeUserRepository(users=users)
    uow = FakeUnitOfWork()
    service = AuthorizeUser(user_repository, uow)
    req = AuthorizeUserRequest(id=user.id, password=user.password)

    # when
    res = service.execute(req)

    # then
    assert res == AuthorizeUserResponse(id=user.id, name=user.name)
