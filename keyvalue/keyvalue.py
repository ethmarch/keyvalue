from abc import ABC, abstractmethod

class KeyValueStore(ABC):

    @abstractmethod
    def set(self, key: str, value: str) -> None:
        pass

    @abstractmethod
    def get(self, key: str) -> str:
        pass

