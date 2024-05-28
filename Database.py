from abc import ABC, abstractmethod
import sqlite3

class Database(ABC):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object().__new__(cls)
        return cls.__instance
    
    def __init__(self, dbName: str):
        self.DBName = dbName
        self.create()
    
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
    def create(self) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS User 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            position VARCHAR(255) NOT NULL)''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def insert(self, values: list) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''INSERT INTO User (name, email, password, position)
            VALUES (?, ?, ?, ?)''', (values))
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print(f"An unknown error has occurred.")
        finally:
            if connection:
                connection.close()

    def read(self, userID: int) -> dict:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''SELECT * FROM User WHERE id = {userID}''')
            result = cursor.fetchone()
            if result:
                return {'id': result[0], 'name': result[1], 'email': result[2], 'password': result[3], 'position': result[4]}
            else:
                return dict()
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
            return dict()
        except:
            print("An unknown error has occurred.")
            return dict()
        finally:
            if connection:
                connection.close()

    def update(self, userID: int, values: dict) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            set_string = ', '.join([f"{k} = '{v}'" for k,v in values.items()])
            update_query = f'''UPDATE User SET {set_string} WHERE id = {userID}'''
            cursor.execute(update_query)
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def delete(self, userID: int) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''DELETE FROM User WHERE id = {userID}''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()

    def getUserByEmailAndPassword(self, userEmail: str, userPassword: str) -> dict:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM User WHERE email = ? AND password = ?''', (userEmail, userPassword))
            result = cursor.fetchone()
            if result:
                return {'id': result[0], 'name': result[1], 'email': result[2], 'password': result[3], 'position': result[4]}
            else:
                return dict()
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
            return dict()
        except:
            print("An unknown error has occurred.")
            return dict()
        finally:
            if connection:
                connection.close()

class ClientsDBDAO(Database):
    def create(self) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Client 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            company VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL)''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def insert(self, values: list) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Client (name, email, password, company, phone)
            VALUES (?, ?, ?, ?, ?)''', (values))
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()

    def read(self, clientID: int) -> dict:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''SELECT * FROM Client WHERE id = {clientID}''')
            result = cursor.fetchone()
            if result:
                return {'id': result[0], 'name': result[1], 'email': result[2], 'password': result[3], 'company': result[4], 'phone': result[5]}
            else:
                return dict()
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
            return dict()
        except:
            print("An unknown error has occurred.")
            return dict()
        finally:
            if connection:
                connection.close()
    
    def update(self, clientID: int, values: dict) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            set_string = ', '.join([f"{k} = '{v}'" for k,v in values.items()])
            update_query = f'''UPDATE Client SET {set_string} WHERE id = {clientID}'''
            cursor.execute(update_query)
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()

    def delete(self, clientID: int) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''DELETE FROM Client WHERE id = {clientID}''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()

    def getClientByEmailAndPassword(self, clientEmail: str, clientPassword: str) -> dict:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM Client WHERE email = ? AND password = ?''', (clientEmail, clientPassword))
            result = cursor.fetchone()
            if result:
                return {'id': result[0], 'name': result[1], 'email': result[2], 'password': result[3], 'company': result[4], 'phone': result[5]}
            else:
                return dict()
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
            return dict()
        except:
            print("An unknown error has occurred.")
            return dict()
        finally:
            if connection:
                connection.close()

class ProblemsDBDAO(Database):
    def create(self) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Problem 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            sla VARCHAR(255) NOT NULL, 
            description VARCHAR(255) NOT NULL)''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def insert(self, values: list) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Problem (sla, description)
            VALUES (?, ?)''', (values))
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def read(self, problemID: int) -> dict:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''SELECT * FROM Problem WHERE id = {problemID}''')
            result = cursor.fetchone()
            if result:
                return {'id': result[0], 'sla': result[1], 'description': result[2]}
            else:
                return dict()
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
            return dict()
        except:
            print("An unknown error has occurred.")
            return dict()
        finally:
            if connection:
                connection.close()
    
    def update(self, problemID: int, values: dict) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            set_string = ', '.join([f"{k} = '{v}'" for k,v in values.items()])
            update_query = f'''UPDATE Problem SET {set_string} WHERE id = {problemID}'''
            cursor.execute(update_query)
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def delete(self, problemID: int) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''DELETE FROM Problem WHERE id = {problemID}''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")  
        finally:
            if connection:
                connection.close()

class CallsDBDAO(Database):
    def create(self) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Call 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            clientID INT,
            userID INT,
            status VARCHAR(255) NOT NULL,
            openingDate VARCHAR(255) NOT NULL,
            closingDate VARCHAR(255) NOT NULL,
            maxDate VARCHAR(255) NOT NULL)''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def insert(self, values: list) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Call (title, description, 
            category, clientID, userID, status, openingDate, closingDate, maxDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (values))
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def read(self, callID: int) -> dict:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''SELECT * FROM Call WHERE id = {callID}''')
            result = cursor.fetchone()
            if result:
                return {'id': result[0], 'title': result[1], 'description': result[2],
                        'category': result[3], 'clientID': result[4], 'userID': result[5],
                        'status': result[6], 'openingDate': result[7], 
                        'closingDate': result[8], 'maxDate': result[9]}
            else:
                return dict()
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
            return dict()
        except:
            print("An unknown error has occurred.")
            return dict()
        finally:
            if connection:
                connection.close()
    
    def update(self, callID: int, values: dict) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            set_string = ', '.join([f"{k} = '{v}'" for k,v in values.items()])
            update_query = f'''UPDATE Call SET {set_string} WHERE id = {callID}'''
            cursor.execute(update_query)
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
    
    def delete(self, callID: int) -> None:
        connection = None
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''DELETE FROM Call WHERE id = {callID}''')
            connection.commit()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
        finally:
            if connection:
                connection.close()
