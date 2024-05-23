import datetime
from Database import CallsDBDAO
from dataclasses import dataclass

@dataclass
class Call():
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

    def __init__(self):
        self.DAO = CallsDBDAO()

    def open(self):
        # Simula a abertura de um chamado e salva no banco de dados
        print(f"Chamado '{self.title}' aberto.")
        # Aqui você iria interagir com o banco de dados

    def assignUser(self, user_id):
        self.user_id = user_id
        print(f"Usuário {user_id} atribuído ao chamado '{self.title}'.")
        # Aqui você iria atualizar o banco de dados

    def changeStatus(self, status):
        self.status = status
        print(f"Status do chamado '{self.title}' alterado para '{status}'.")
        # Aqui você iria atualizar o banco de dados

    def close(self):
        self.status = 'fechado'
        self.closing_date = datetime.datetime.now()
        print(f"Chamado '{self.title}' fechado.")
        # Aqui você iria atualizar o banco de dados

    def view(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'client_id': self.client_id,
            'user_id': self.user_id,
            'status': self.status,
            'opening_date': self.opening_date,
            'max_date': self.max_date,
            'closing_date': self.closing_date
        }

    def update(self, title=None, description=None, category=None, client_id=None, user_id=None, status=None, max_date=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if category:
            self.category = category
        if client_id:
            self.client_id = client_id
        if user_id:
            self.user_id = user_id
        if status:
            self.status = status
        if max_date:
            self.max_date = max_date
        print(f"Chamado '{self.title}' atualizado.")
        # Aqui você iria atualizar o banco de dados

    def delete(self):
        print(f"Chamado '{self.title}' deletado.")
        # Aqui você iria deletar o chamado do banco de dados

