import datetime
from Database import CallsDBDAO
from dataclasses import dataclass

@dataclass
class Calls():
    id: int
    title: str
    description: str
    category: str
    clientID: int
    userID: int
    status: str
    openingDate: str
    closingDate: str
    maxDate: str
    
class CallsManager():
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object().__new__(cls)
        return cls.__instance

    def __init__(self, dbName: str):
        self.DAO = CallsDBDAO(dbName)

    def open(self, call: Calls) -> None:
        self.DAO.insert([call.id, call.title, call.description, call.category,
                         call.clientID, call.userID, call.status, call.openingDate,
                         call.closingDate, call.maxDate])

    def assignUser(self, callID: int, userID: int) -> None:
        self.DAO.update(callID, {'userID': userID})
        
    def changeStatus(self, callID: int, status: str) -> None:
        self.DAO.update(callID, {'status': status})

    def close(self, callID: int) -> None:
        closingDate = str(datetime.datetime.now())
        self.DAO.update(callID, {'status': "closed", 'closingDate': closingDate})

    def view(self, callID: int) -> None:
        data = self.DAO.read(callID)
        print(f"ID: {data['id']}\n\
                Title: {data['title']}\n\
                Description: {data['description']}\n\
                Category: {data['category']}\n\
                Client ID: {data['clientID']}\n\
                User ID: {data['userID']}\n\
                Status: {data['status']}\n\
                Opening Date: {data['openingDate']}\n\
                Closing Date: {data['closingDate']}\n\
                Max Date: {data['maxDate']}")

    def update(self, callID: int, updateData: dict) -> None:
        self.DAO.update(callID, updateData)

    def delete(self, callID: int) -> None:
        self.DAO.delete(callID)

