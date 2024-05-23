from abc import ABC, abstractmethod
import sqlite3

class Database(ABC):
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

'''
As DBDAOs receberão dados através de uma lista

'''


class UsersDBDAO(Database):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(UsersDBDAO, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    
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
    
    def read(self, user_id: int) -> dict:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = ?''', (client_id,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return {'ID': result[0], 'Name': result[1], 'Email': result[2], 'Password': result[3], 'Position': result[4]}
        else:
            return {}
    
    def update(self, user_id: int, values: dict) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        update_query = '''UPDATE User SET Name = ?, Email = ?, Password = ?, Position = ? WHERE ID = ?'''
        cursor.execute(update_query, (values['Name'], values['Email'], values['Password'], values['Position'], client_id))
        connection.commit()
        connection.close()
    
    def delete(self, user_id: int) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM User WHERE ID = ?''', (client_id,))
        connection.commit()
        connection.close()



class ClientsDBDAO(Database):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(ClientsDBDAO, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    def __init__(self) -> None:
        self.DBName = "clients.db"
        self.create()
    import sqlite3

class ClientDatabase:
    def __init__(self, DBName: str):
        self.DBName = DBName

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
    
    def read(self, client_id: int) -> dict:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Client WHERE id = ?''', (client_id,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return {'id': result[0], 'name': result[1], 'email': result[2], 'company': result[3], 'phone': result[4]}
        else:
            return {}
    
    def update(self, client_id: int, values: dict) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        update_query = '''UPDATE Client SET name = ?, email = ?, company = ?, phone = ? WHERE id = ?'''
        cursor.execute(update_query, (values['name'], values['email'], values['company'], values['phone'], client_id))
        connection.commit()
        connection.close()
    
    def delete(self, client_id: int) -> None:
        connection = sqlite3.connect(self.DBName)
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM Client WHERE id = ?''', (client_id,))
        connection.commit()
        connection.close()    

class ProblemsDBDAO(Database):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(ProblemsDBDAO, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
