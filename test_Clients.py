import pytest
import os
import sqlite3
from Clients import *
from dataclasses import asdict

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "clientTest.db"

@pytest.fixture(scope="module")
def clientsManager():
    silentRemove(databaseName)
    clientManager = ClientsManager(databaseName)
    clientManager.register(Clients('Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    yield clientManager
    silentRemove(databaseName)

def test_createClient():
    client = Clients('Client 1', 'client1@example.com', 'password123', 'Company A', '123456789')
    data = asdict(client)
    assert data == {'name': 'Client 1', 'email': 'client1@example.com', 'password': 'password123', 'company': 'Company A', 'phone': '123456789'}

def test_register(clientsManager):
    clientsManager.register(Clients('Client 2', 'client2@example.com', 'password321', 'Company B', '987654321'))
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Client WHERE ID = 2''')
        assert cursor.fetchone() == (2, 'Client 2', 'client2@example.com', 'password321', 'Company B', '987654321')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_update(clientsManager):
    newData = {'name': 'Client Updated', 'email': 'updated@example.com', 'password': 'newpassword', 'company': 'New Company'}
    clientsManager.update(1, newData)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Client WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Client Updated', 'updated@example.com', 'newpassword', 'New Company', '123456789')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_delete(clientsManager):
    userID = 1
    clientsManager.delete(userID)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Client WHERE ID = 1''')
        assert cursor.fetchone() is None
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_isValid(clientsManager):
    assert clientsManager.isValid("client1@example.com", "password123")
    assert not clientsManager.isValid("cl@example.com", "password123")
    assert not clientsManager.isValid("client1@example.com", "password")
    assert not clientsManager.isValid("cl@example.com", "password")

def test_getByEmailAndPassword(clientsManager):
    data = clientsManager.getByEmailAndPassword("client1@example.com", "password123")
    assert data == {'id': 1, 'name': 'Client 1', 'email': 'client1@example.com', 'password': 'password123', 'company': 'Company A', 'phone': '123456789'}
    assert clientsManager.getByEmailAndPassword("client2@example.com", "password") == {}