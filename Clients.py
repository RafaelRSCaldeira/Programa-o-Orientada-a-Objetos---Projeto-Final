from Database import *
from Manager import Manager

class Clients():
    def __init__(self, id: int, name: str, email: str, password: str, position: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.company = company
        self.phone = phone


class ClientsManager(Manager):
    def __init__(self):
        self.DAO = UsersDBDAO()

    def createClient(self):
        
    
    def register(self, user: Users):
        pass

    def view(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass

'''
As funções precisam:
    criar conexão com banco de dados;
    criar cursor da conexão;
    executar comando;
    fazer o "commit" da ação;
    encerrar conexão com o banco de dados.

As interações com o banco de dados ocorrerão 
através das classes DAO
'''