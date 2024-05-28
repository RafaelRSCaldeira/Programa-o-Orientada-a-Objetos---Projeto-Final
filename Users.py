from Database import *
from Manager import Manager
from dataclasses import dataclass
from dataclasses import asdict


@dataclass
class Users():
    id:int
    name: str
    email: str
    password: str
    position: str


class UsersManager(Manager):
    def __init__(self, dbName: str):
        self.DAO = UsersDBDAO(dbName)
    
    def register(self, user: Users) -> None:
        self.DAO.insert([user.name, user.email, user.password, user.position])
        
    def view(self, userID: int) -> None:
        data = self.DAO.read(userID)
        print(f"ID: {data['id']}\n\
                Name: {data['name']}\n\
                Email: {data['email']}\n\
                Position: {data['position']}")
    
    #Modificado para adicionar o ID
    def update(self,updateUser: Users) -> None:
        updateData = asdict(updateUser)
        del updateData['id']
        self.DAO.update(updateUser.id, updateData)

    def delete(self, userID: int) -> None:
        self.DAO.delete(userID)

    def isValid(self, userEmail: str, userPassword: str) -> bool:
        data = self.DAO.getUserByEmailAndPassword(userEmail, userPassword)
        if len(data) == 0:
            return False
        return True

    #Modificado para se não houver um valido
    def getByEmailAndPassword(self, userEmail: str, userPassword: str) -> Users:
        data = self.DAO.getUserByEmailAndPassword(userEmail, userPassword)
        if(len(data) == 0):
           return None
        return Users(data.get('name'), data.get('email'), data.get('password'), data.get('position'))

    #Modificado para caso não haja dados
    def getByID(self, userID: int) -> Users|None:
        data =  self.DAO.read(userID)
        if(len(data) == 0):
           return None
        return Users(data.get('id'), data.get('name'), data.get('email'), data.get('password'), data.get('position'))
    
    #Adicionado metodo getAllIds
    def getAllIds(self) -> list:
        ids = []
        for i in self.DAO.getAllIds():
            ids.append(i[0])
        return ids