from abc import ABC, abstractmethod
import sqlite3

class Manager(ABC):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object().__new__(cls)
        return cls.__instance

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass



