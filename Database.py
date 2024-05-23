from abc import ABC, abstractmethod
import sqlite3

class Database(ABC):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object().__new__(cls)
        return cls.__instance
    
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def insert():
        pass

    @abstractmethod
    def read():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass

class UsersDBDAO(Database):    
    def __init__(self) -> None:
        self.DBName = "users.db"
        self.create()
    
    def create(self) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS User 
        (ID INT PRIMARY KEY, 
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        Password VARCHAR(255) NOT NULL,
        Position VARCHAR(255) NOT NULL''')
        connection.commit()
        connection.close()
    
    def insert(self, values: list) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO User (ID, Name, Email, Password, Position)
        VALUES ({values[0]},{values[1]},{values[2]},{values[3]},{values[5]})''')
        connection.commit()
        connection.close()
    
    def read(self, userID: int) -> dict:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = ?''', (userID,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return {'ID': result[0], 'Name': result[1], 'Email': result[2], 'Password': result[3], 'Position': result[4]}
        else:
            return {}
    
    def update(self, userID: int, values: dict) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        update_query = '''UPDATE User SET Name = ?, Email = ?, Password = ?, Position = ? WHERE ID = ?'''
        cursor.execute(update_query, (values['Name'], values['Email'], values['Password'], values['Position'], userID))
        connection.commit()
        connection.close()
    
    def delete(self, userID: int) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM User WHERE ID = ?''', (userID,))
        connection.commit()
        connection.close()



class ClientsDBDAO(Database):
    def __init__(self) -> None:
        self.DBName = "clients.db"
        self.create()

    def create(self) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Client 
        (id INT PRIMARY KEY, 
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        company VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL)''')
        connection.commit()
        connection.close()
    
    def insert(self, values: list) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO Client (id, name, email, company, phone)
        VALUES (?, ?, ?, ?, ?)''', (values[0], values[1], values[2], values[3], values[4]))
        connection.commit()
        connection.close()
    
    def read(self, clientID: int) -> dict:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Client WHERE id = ?''', (clientID,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return {'id': result[0], 'name': result[1], 'email': result[2], 'company': result[3], 'phone': result[4]}
        else:
            return {}
    
    def update(self, clientID: int, values: dict) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        update_query = '''UPDATE Client SET name = ?, email = ?, company = ?, phone = ? WHERE id = ?'''
        cursor.execute(update_query, (values['name'], values['email'], values['company'], values['phone'], clientID))
        connection.commit()
        connection.close()
    
    def delete(self, clientID: int) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM Client WHERE id = ?''', (clientID,))
        connection.commit()
        connection.close()    

class ProblemsDBDAO(Database):
    def __init__(self) -> None:
        self.DBName = "problems.db"
        self.create()

    def create(self) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Problem 
        (id INT PRIMARY KEY,
        sla VARCHAR(255) NOT NULL, 
        description VARCHAR(255) NOT NULL)''')
        connection.commit()
        connection.close()
    
    def insert(self, values: list) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO Problem (id, sla, description)
        VALUES (?, ?, ?)''', (values[0], values[1], values[2]))
        connection.commit()
        connection.close()
    
    def read(self, problemID: int) -> dict:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Problem WHERE id = ?''', (problemID,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return {'id': result[0], 'sla': result[1], 'description': result[2]}
        else:
            return {}
    
    def update(self, problemID: int, values: dict) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        update_query = '''UPDATE Client SET sla = ?, description = ? WHERE id = ?'''
        cursor.execute(update_query, (values['sla'], values['description'], problemID))
        connection.commit()
        connection.close()
    
    def delete(self, problemID: int) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM Client WHERE id = ?''', (problemID))
        connection.commit()
        connection.close()  
