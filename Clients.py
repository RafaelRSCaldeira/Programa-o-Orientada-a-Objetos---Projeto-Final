from Database import *
from Manager import Manager
from Person import Person

class Clients(Person):
    def __init__(self, company: str, phone: int) -> None:
        super().__init__(id, name, email)
        self.company = company
        self.phone = phone


class ClientsManager(Manager):
    def __init__(self):
        self.DAO = UsersDBDAO()

    def createClient(self):
        pass
    
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
