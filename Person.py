from abc import ABC, abstractmethod
import sqlite3


class Person(ABC):
    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.connect = sqlite3.connect()
        self.cursor = self.connect.cursor()
    
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
