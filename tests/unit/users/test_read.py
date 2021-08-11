from app.users.service_layer.read import read_user, ReadUserRequest, ReadUserResponse, read_users, ReadUsersResponse
from tests.unit.users.conftest import get_fake_user, get_fake_users
from tests.unit.users.fake_repository import FakeUserRepository


def test_read_user():
    # given
    fake_user_repository = FakeUserRepository([get_fake_user()])
    req = ReadUserRequest(id="hardy@socar.kr")

    # when
    res = read_user(req, fake_user_repository)

    # then
    assert res == ReadUserResponse(id="hardy@socar.kr", name="hardy")


def test_read_users():
    # given
    fake_user_repository = FakeUserRepository(get_fake_users())

    # when
    res = read_users(fake_user_repository)

    # then
    assert res == ReadUsersResponse(
        items=[
            ReadUserResponse(**{"id": "hardy@socar.kr", "name": "hardy"}),
            ReadUserResponse(**{"id": "knox@socar.kr", "name": "knox"}),
            ReadUserResponse(**{"id": "humphrey@socar.kr", "name": "humphrey"}),
        ]
    )
