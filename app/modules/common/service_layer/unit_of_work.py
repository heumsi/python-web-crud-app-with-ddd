from abc import ABC, abstractmethod
from types import TracebackType
from typing import Type


class UnitOfWork(ABC):
    def __exit__(
        self, exc_type: Type[Exception], exc_val: Exception, exc_tb: TracebackType
    ) -> None:
        if exc_type:
            self.rollback()

    def __enter__(self) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass
