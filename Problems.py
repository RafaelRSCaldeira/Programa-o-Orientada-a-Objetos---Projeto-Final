from Database import *
from Manager import Manager
from datetime import timedelta

class Problems():
    def __init__(self, id: int, description: str, sla:int) -> None:
        self.id = id
        self.description = description
        self.sla = timedelta(horas=sla.hours)

class ProblemsManager(Manager):
    def __init__(self):
        self.DAO = ProblemsDBDAO() #define a classe ProblemsDBDAO como DAO
    
    def register(self, problem: Problem):   #chama a função dao para se conectar com o banco de dados dos problemas e registrar um prblema
        self.DAO.insert(problem.id,problem.description,problem.sla)
        
    def view(self, problem: Problem):
        pass
    
    def update(self, problem: Problem):   #chama a função dao para se conectar com o banco de dados dos problemas e atualizar um problema
        self.DAO.update(problem.id, problem.description, problem.sla)

    def delete(self, problem: Problem):  #chama a função dao para se conectar com o banco de dados dos problemas e deletar um problema
        self.DAO.delete(problem.id)
    
    def priority(self, problem: Problem, sla : int):
        pass

    def problemcategory(self, problem: Problem, category):
        pass
