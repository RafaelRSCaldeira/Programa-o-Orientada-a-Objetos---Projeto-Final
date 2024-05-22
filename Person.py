from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email
    
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
