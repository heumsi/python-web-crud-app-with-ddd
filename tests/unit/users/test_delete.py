from app.modules.users.service_layer.use_cases.delete import (
    DeleteUser,
    DeleteUserRequest,
)
from tests.unit.users.conftest import get_fake_user
from tests.unit.users.fake_repository import FakeUserRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_delete_user():
    # given
    uow = FakeUnitOfWork()
    user_repository = FakeUserRepository([get_fake_user()])
    req = DeleteUserRequest(id="hardy@socar.kr")
    service = DeleteUser(user_repository=user_repository, uow=uow)

    # when
    service.execute(req)

    # then
    assert user_repository.find_all() == []
    assert uow.committed
