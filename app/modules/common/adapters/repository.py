from abc import abstractmethod, ABC

from dataset import Table, Database


class DatasetRepository(ABC):
    def __init__(self, db: Database) -> None:
        self._db = db

    def get_table(self) -> Table:
        table: Table = self._db.get_table(self.table_name)
        return table

    @property
    @abstractmethod
    def table_name(self) -> str:
        pass
