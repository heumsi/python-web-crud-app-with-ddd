from dataset import Database

from app.infrastructures.persistence import create_tables
from app.modules.common.service_layer.unit_of_work import DatasetUnitOfWork
from app.modules.users.adapters.repository import DatasetUserRepository
from tests.unit.users.conftest import get_fake_user

db = Database(url="sqlite://")
create_tables(db)

user_repository = DatasetUserRepository(db)


def test_uow_can_add_user():
    # given
    uow = DatasetUnitOfWork(db=db)
    user = get_fake_user()

    # when
    with uow:
        user_repository.save(user)
        uow.commit()

    # then
    with db as tx:
        table = tx.get_table("user")
        assert list(table.all()) == [user]
