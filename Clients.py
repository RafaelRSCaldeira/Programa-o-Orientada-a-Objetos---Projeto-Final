from Database import *
from Manager import Manager
from dataclasses import dataclass

@dataclass
class Clients():
    name: str
    email: str
    password: str
    company: str
    phone: str

class ClientsManager(Manager):
    def __init__(self, dbName: str):
        self.DAO = ClientsDBDAO(dbName)
    
    def register(self, client: Clients) -> None:
        self.DAO.insert([client.name, client.email, client.password, client.company, client.phone])

    def view(self, clientID: int) -> None:
        data = self.DAO.read(clientID)
        print(f"ID: {data['id']}\n\
                Name: {data['name']}\n\
                Email: {data['email']}\n\
                Company: {data['company']}\n\
                Phone: {data['phone']}")
    
    def update(self, clientID: int, updateData: dict) -> None:
        self.DAO.update(clientID, updateData)

    def delete(self, clientID: int) -> None:
        self.DAO.delete(clientID)

    def isValid(self, clientEmail: str, clientPassword: str) -> bool:
        data = self.DAO.getClientByEmailAndPassword(clientEmail, clientPassword)
        if len(data) == 0:
            return False
        return True

