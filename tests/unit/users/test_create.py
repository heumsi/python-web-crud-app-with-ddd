from app.users.service_layer.create import CreateUserRequest, create_user, CreateUserResponse
from tests.unit.users.fake_repository import FakeUserRepository


def test_create_user():
    # given
    fake_user_repository = FakeUserRepository()
    req = CreateUserRequest(id="hardy@socar.kr", name="hardy", password="1234")

    # when
    res = create_user(req, fake_user_repository=fake_user_repository)

    # then
    assert res == CreateUserResponse(id="hardy@socar.kr", name="hardy")
