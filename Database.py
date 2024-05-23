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
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS User 
            (id INT PRIMARY KEY, 
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            position VARCHAR(255) NOT NULL''')
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def insert(self, values: list) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute(f'''INSERT INTO User (id, name, email, password, position)
            VALUES ({values[0]},{values[1]},{values[2]},{values[3]},{values[5]})''')
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def read(self, userID: int) -> dict:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM User WHERE ID = ?''', (userID,))
            result = cursor.fetchone()
            connection.close()
            if result:
                return {'id': result[0], 'name': result[1], 'email': result[2], 'password': result[3], 'position': result[4]}
            else:
                return {}
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def update(self, userID: int, values: dict) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            update_query = '''UPDATE User SET name = ?, email = ?, password = ?, position = ? WHERE id = ?'''
            cursor.execute(update_query, (values['name'], values['email'], values['password'], values['position'], userID))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def delete(self, userID: int) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM User WHERE id = ?''', (userID,))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")   



class ClientsDBDAO(Database):
    def __init__(self) -> None:
        self.DBName = "clients.db"
        self.create()

    def create(self) -> None:
        try:
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
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def insert(self, values: list) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Client (id, name, email, company, phone)
            VALUES (?, ?, ?, ?, ?)''', (values[0], values[1], values[2], values[3], values[4]))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print("An unknown error has occurred.")

    def read(self, clientID: int) -> dict:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM Client WHERE id = ?''', (clientID,))
            result = cursor.fetchone()
            connection.close()
            if result:
                return {'id': result[0], 'name': result[1], 'email': result[2], 'company': result[3], 'phone': result[4]}
            else:
                return {}
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def update(self, clientID: int, values: dict) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            update_query = '''UPDATE Client SET name = ?, email = ?, company = ?, phone = ? WHERE id = ?'''
            cursor.execute(update_query, (values['name'], values['email'], values['company'], values['phone'], clientID))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")

    def delete(self, clientID: int) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM Client WHERE id = ?''', (clientID,))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")    

class ProblemsDBDAO(Database):
    def __init__(self) -> None:
        self.DBName = "problems.db"
        self.create()

    def create(self) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Problem 
            (id INT PRIMARY KEY,
            sla VARCHAR(255) NOT NULL, 
            description VARCHAR(255) NOT NULL)''')
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def insert(self, values: list) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Problem (id, sla, description)
            VALUES (?, ?, ?)''', (values[0], values[1], values[2]))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def read(self, problemID: int) -> dict:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM Problem WHERE id = ?''', (problemID,))
            result = cursor.fetchone()
            connection.close()
            if result:
                return {'id': result[0], 'sla': result[1], 'description': result[2]}
            else:
                return {}
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def update(self, problemID: int, values: dict) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            update_query = '''UPDATE Problem SET sla = ?, description = ? WHERE id = ?'''
            cursor.execute(update_query, (values['sla'], values['description'], problemID))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def delete(self, problemID: int) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM Problem WHERE id = ?''', (problemID))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")  

class CallsDBDAO(Database):
    def __init__(self) -> None:
        self.DBName = "calls.db"
        self.create()

    def create(self) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Call 
            (id INT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            clientID INT FOREIGN KEY,
            userID INT FOREIGN KEY,
            status: VARCHAR(255) NOT NULL,
            openingDate VARCHAR(255) NOT NULL,
            closingDate VARCHAR(255) NOT NULL,
            maxDate VARCHAR(255) NOT NULL)''')
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to create the table. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def insert(self, values: list) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Problem (id, title, description, 
            category, clientID, userID, status, openingDate, closingDate, maxDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (values[0], values[1], values[2],
            values[3], values[4], values[5], values[6], values[7], values[8], values[9]))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to insert data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def read(self, callID: int) -> dict:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM Call WHERE id = ?''', (callID,))
            result = cursor.fetchone()
            connection.close()
            if result:
                return {'id': result[0], 'title': result[1], 'description': result[2],
                        'category': result[3], 'clientID': result[4], 'userID': result[5],
                        'status': result[6], 'openingDate': result[7], 
                        'closingDate': result[8], 'maxDate': result[9]}
            else:
                return {}
        except sqlite3.Error as error:
            print(f"Unable to fetch the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def update(self, callID: int, values: dict) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            update_query = '''UPDATE Call SET title = ?,
            description = ?, category = ?, clientID = ?,
            userID = ?, status = ?, openingDate = ?, closingDate = ?,
            maxDate = ? WHERE id = ?'''
            cursor.execute(update_query, (values['title'], values['description'],
                                          values['category'], values['clientID'],
                                          values['userID'], values['status'],
                                          values['openingDate'], values['closingDate'],
                                          values['maxDate'], callID))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to update the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")
    
    def delete(self, callID: int) -> None:
        try:
            connection = sqlite3.connect(self.DBName)
            cursor = connection.cursor()
            cursor.execute('''DELETE FROM Call WHERE id = ?''', (callID))
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(f"Unable to delete the data. Error: {error}.")
        except:
            print("An unknown error has occurred.")  
