from app.users.service_layer.delete import DeleteUserRequest, delete_user
from tests.unit.users.conftest import get_fake_user
from tests.unit.users.fake_repository import FakeUserRepository


def test_delete_user():
    # given
    fake_user_repository = FakeUserRepository([get_fake_user()])
    req = DeleteUserRequest(id="hardy@socar.kr")

    # when
    res = delete_user(req, fake_user_repository)

    # then
    assert res == None
