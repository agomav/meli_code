from abc import (
    ABCMeta,
    abstractmethod
)


class ItemRepositoryInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, item):
        pass