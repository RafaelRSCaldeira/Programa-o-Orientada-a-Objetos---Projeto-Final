from Database import *
from Manager import Manager

class Problems():
    def __init__(self, id: int, name: str, email: str, password: str, position: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.position = position


class UsersManager(Manager):
    def __init__(self):
        self.DAO = UsersDBDAO()
    
    def register(self, user: Users):
        self.DAO.insert(user.id, user.name, user.email, user.password, user.position)
        
    def view(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass
