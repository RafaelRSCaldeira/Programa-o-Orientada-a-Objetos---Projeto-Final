from Database import *
from Manager import Manager
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class Clients():
    id: int
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
    
    #Modificado para adicionar ID
    def update(self, updateClient: Clients) -> None:
        updateData = asdict(updateClient)
        del updateClient['id']
        self.DAO.update(updateClient.id, updateData)

    def delete(self, clientID: int) -> None:
        self.DAO.delete(clientID)

    def isValid(self, clientEmail: str, clientPassword: str) -> bool:
        data = self.DAO.getClientByEmailAndPassword(clientEmail, clientPassword)
        if len(data) == 0:
            return False
        return True

    #Modificado para caso não haja dados e adicionar ID
    def getByEmailAndPassword(self, clientEmail: str, clientPassword: str) -> Clients:
        data = self.DAO.getClientByEmailAndPassword(clientEmail, clientPassword)
        if(len(data) == 0):
           return None
        return Clients(data.get('id'), data.get('name'), data.get('email'), data.get('password'), data.get('company'), data.get('phone'))
    
    #Modificado para caso não haja dados
    def getByID(self, clientID: int) -> Clients|None:
        data =  self.DAO.read(clientID)
        if(len(data) == 0):
           return None
        return Clients(data.get('id'), data.get('name'), data.get('email'), data.get('password'), data.get('company'), data.get('phone'))
    
    #Adicionado metodo getAllIds
    def getAllIds(self) -> list:
        ids = []
        for i in self.DAO.getAllIds():
            ids.append(i[0])
        return ids