from Database import *
from Manager import Manager
from dataclasses import dataclass

@dataclass
class Users():
    id: int
    name: str
    email: str
    password: str
    position: str


class UsersManager(Manager):
    def __init__(self):
        self.DAO = UsersDBDAO()
    
    def register(self, user: Users) -> None:
        self.DAO.insert([user.id, user.name, user.email, user.password, user.position])
        
    def view(self, userID: int) -> None:
        data = self.DAO.read(userID)
        print(f"ID: {data['id']}\n\
                Name: {data['name']}\n\
                Email: {data['email']}\n\
                Position: {data['position']}")
    
    def update(self, userID: int, updateData: dict) -> None:
        self.DAO.update(userID, updateData)

    def delete(self, userID: int) -> None:
        self.DAO.delete(userID)

