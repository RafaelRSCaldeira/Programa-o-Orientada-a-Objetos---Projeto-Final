from Database import *
from Manager import Manager
from dataclasses import dataclass
from dataclasses import asdict

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
    
    def update(self, clientID: int, updateClient: Clients) -> None:
        updateData = asdict(updateClient)
        self.DAO.update(clientID, updateData)

    def delete(self, clientID: int) -> None:
        self.DAO.delete(clientID)

    def isValid(self, clientEmail: str, clientPassword: str) -> bool:
        data = self.DAO.getClientByEmailAndPassword(clientEmail, clientPassword)
        if len(data) == 0:
            return False
        return True

    def getByEmailAndPassword(self, clientEmail: str, clientPassword: str) -> Clients:
        data = self.DAO.getClientByEmailAndPassword(clientEmail, clientPassword)
        return Clients(data.get('name'), data.get('email'), data.get('password'), data.get('company'), data.get('phone'))
    
    def getByID(self, clientID: int) -> Clients:
        data =  self.DAO.read(clientID)
        return Clients(data.get('name'), data.get('email'), data.get('password'), data.get('company'), data.get('phone'))
