from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def view(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass

class Client(Person):
    def __init__(self, id, name, email, company, phone):
        super().__init__(id, name, email)
        self.company = company
        self.phone = phone
    
    def register(self):
        # Implementação específica para o registro de um cliente
        pass
    
    def view(self):
        # Implementação específica para a visualização de um cliente
        pass
    
    def update(self):
        # Implementação específica para a atualização de um cliente
        pass
    
    def delete(self):
        # Implementação específica para a exclusão de um cliente
        pass

class User(Person):
    def __init__(self, id, name, email, password, position):
        super().__init__(id, name, email)
        self.password = password
        self.position = position
    
    def register(self):
        # Implementação específica para o registro de um usuário
        pass
    
    def view(self):
        # Implementação específica para a visualização de um usuário
        pass
    
    def update(self):
        # Implementação específica para a atualização de um usuário
        pass
    
    def delete(self):
        # Implementação específica para a exclusão de um usuário
        pass

