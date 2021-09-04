from app.modules.users.service_layer.use_cases.read import (
    ReadUser,
    ReadUserRequest,
    ReadUserResponse,
    ReadUsers,
    ReadUsersResponse,
)
from tests.unit.users.conftest import get_fake_user, get_fake_users
from tests.unit.users.fake_repository import FakeUserRepository
from tests.unit.users.fake_unit_of_work import FakeUnitOfWork


def test_read_user():
    # given
    uow = FakeUnitOfWork()
    user_repository = FakeUserRepository([get_fake_user()])
    req = ReadUserRequest(id="hardy@socar.kr")
    service = ReadUser(user_repository=user_repository, uow=uow)

    # when
    res = service.execute(req)

    # then
    assert res == ReadUserResponse(id="hardy@socar.kr", name="hardy")
    assert uow.committed is False


def test_read_users():
    # given
    uow = FakeUnitOfWork()
    user_repository = FakeUserRepository(get_fake_users())
    service = ReadUsers(user_repository=user_repository, uow=uow)

    # when
    res = service.execute()

    # then
    assert res == ReadUsersResponse(
        items=[
            ReadUserResponse(**{"id": "hardy@socar.kr", "name": "hardy"}),
            ReadUserResponse(**{"id": "knox@socar.kr", "name": "knox"}),
            ReadUserResponse(**{"id": "humphrey@socar.kr", "name": "humphrey"}),
        ]
    )
    assert uow.committed is False
