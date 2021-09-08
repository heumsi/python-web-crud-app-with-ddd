from dataset import Database

from app.modules.common.service_layer.unit_of_work import UnitOfWork


class DatasetUnitOfWork(UnitOfWork):
    def __init__(self, db: Database) -> None:
        self.db = db
        self._transaction_depth = 0

    def __enter__(self) -> Database:
        self._transaction_depth += 1
        if not self.db.in_transaction:
            self.db.begin()
        return self.db

    def commit(self) -> None:
        self._transaction_depth -= 1
        if self._transaction_depth == 0:
            self.db.commit()

    def rollback(self) -> None:
        self._transaction_depth -= 1
        self.db.rollback()
