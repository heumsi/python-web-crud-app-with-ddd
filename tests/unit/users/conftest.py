from typing import List

from app.users.domain.model import User


def get_fake_user() -> User:
    return User(id="hardy@socar.kr", name="hardy", password="1234")


def get_fake_users() -> List[User]:
    return [
        User(id="hardy@socar.kr", name="hardy", password="1234"),
        User(id="knox@socar.kr", name="knox", password="4321"),
        User(id="humphrey@socar.kr", name="humphrey", password="1324"),
    ]
