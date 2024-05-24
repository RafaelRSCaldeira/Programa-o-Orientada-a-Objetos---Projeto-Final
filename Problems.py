from Database import *
from Manager import Manager
from datetime import timedelta
from dataclasses import dataclass

@dataclass
class Problems():
    id: int
    description: str
    sla: int

class ProblemsManager(Manager):
    def __init__(self):
        self.DAO = ProblemsDBDAO()
    
    def register(self, problem: Problems) -> None:
        self.DAO.insert([problem.id,problem.description,problem.sla])
        
    def view(self, problemID: int) -> None:
        data = self.DAO.read(problemID)
        print(f"ID: {data['id']}\n\
                Description: {data['description']}\n\
                SLA: {data['sla']}")
    
    def update(self, problemID: int, updateData: dict) -> None:
        self.DAO.update(problemID, updateData)

    def delete(self, problemID: int):
        self.DAO.delete(problemID)
