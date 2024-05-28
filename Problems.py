from Database import *
from Manager import Manager
from datetime import timedelta
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class Problems():
    id: int
    description: str
    sla: int

class ProblemsManager(Manager):
    def __init__(self, dbName: str):
        self.DAO = ProblemsDBDAO(dbName)
    
    def register(self, problem: Problems) -> None:
        self.DAO.insert([problem.description,problem.sla])
        
    def view(self, problemID: int) -> None:
        data = self.DAO.read(problemID)
        print(f"ID: {data['id']}\n\
                Description: {data['description']}\n\
                SLA: {data['sla']}")
    
    #Modificado para ID
    def update(self, updateProblem: Problems) -> None:
        updateData = asdict(updateProblem)
        del updateData['id']
        self.DAO.update(updateProblem.id, updateData)

    def delete(self, problemID: int) -> None:
        self.DAO.delete(problemID)
    
    #Criado getByID
    def getByID(self, problemID: int) -> Problems|None:
        data =  self.DAO.read(problemID)
        if(len(data) == 0):
           return None
        return Problems(data.get('id'), data.get('description'), data.get('sla'))