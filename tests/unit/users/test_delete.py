from app.users.service_layer.delete import DeleteUser, DeleteUserRequest
from tests.unit.users.conftest import get_fake_user
from tests.unit.users.fake_repository import FakeUserRepository


def test_delete_user():
    # given
    fake_user_repository = FakeUserRepository([get_fake_user()])
    req = DeleteUserRequest(id="hardy@socar.kr")
    service = DeleteUser(user_repository=fake_user_repository)

    # when
    service.execute(req)

    # then
    assert fake_user_repository.find_all() == []
