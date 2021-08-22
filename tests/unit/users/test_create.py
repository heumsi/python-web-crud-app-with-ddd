from app.users.service_layer.create import (
    CreateUser,
    CreateUserRequest,
    CreateUserResponse,
)
from tests.unit.users.fake_repository import FakeUserRepository


def test_create_user():
    # given
    fake_user_repository = FakeUserRepository()
    req = CreateUserRequest(id="hardy@socar.kr", name="hardy", password="1234")
    service = CreateUser(user_repository=fake_user_repository)

    # when
    res = service.execute(req)

    # then
    assert res == CreateUserResponse(id="hardy@socar.kr", name="hardy")
    assert len(fake_user_repository.find_all()) == 1
