from app.users.service_layer.create import (
    CreateUser,
    CreateUserRequest,
    CreateUserResponse,
)
from tests.unit.users.fake_repository import FakeUserRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_create_user():
    # given
    uow = FakeUnitOfWork()
    user_repository = FakeUserRepository()
    req = CreateUserRequest(id="hardy@socar.kr", name="hardy", password="1234")
    service = CreateUser(user_repository=user_repository, uow=uow)

    # when
    res = service.execute(req)

    # then
    assert res == CreateUserResponse(id="hardy@socar.kr", name="hardy")
    assert len(user_repository.find_all()) == 1
    assert uow.committed
