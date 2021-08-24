from abc import ABC, abstractmethod

from dataset import Database


class UnitOfWork(ABC):
    def __exit__(self, *args) -> None:
        self.rollback()

    def __enter__(self) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass


class DatasetUnitOfWork(UnitOfWork):
    def __init__(self, db: Database) -> None:
        self.db = db

    def __enter__(self) -> Database:
        self.db.begin()
        return self.db

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()
