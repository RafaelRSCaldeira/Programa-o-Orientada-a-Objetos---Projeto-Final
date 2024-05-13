from abc import ABC, abstractmethod

class Manager(ABC):
    @abstractmethod
    def register():
        pass

    @abstractmethod
    def view():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass