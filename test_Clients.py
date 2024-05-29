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

def test_createClient():
    client = Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789')
    data = asdict(client)
    assert data == {'id': 1, 'name': 'Client 1', 'email': 'client1@example.com', 'password': 'password123', 'company': 'Company A', 'phone': '123456789'}

def test_register():
    silentRemove("clientTest1.db")
    clientManager = ClientsManager("clientTest1.db")
    clientManager.register(Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    conn = None
    try:
        conn = sqlite3.connect("clientTest1.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Client WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("clientTest1.db")

def test_update():
    silentRemove("clientTest2.db")
    clientManager = ClientsManager("clientTest2.db")
    clientManager.register(Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    newClient = Clients(1, 'Client Updated', 'updated@example.com', 'newpassword', 'New Company', '123456789')
    clientManager.update(newClient)
    conn = None
    try:
        conn = sqlite3.connect("clientTest2.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Client WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Client Updated', 'updated@example.com', 'newpassword', 'New Company', '123456789')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("clientTest2.db")

def test_delete():
    silentRemove("clientTest3.db")
    clientManager = ClientsManager("clientTest3.db")
    clientManager.register(Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    userID = 1
    clientManager.delete(userID)
    conn = None
    try:
        conn = sqlite3.connect("clientTest3.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Client WHERE ID = 1''')
        assert cursor.fetchone() is None
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("clientTest3.db")

def test_isValid():
    silentRemove("clientTest4.db")
    clientManager = ClientsManager("clientTest4.db")
    clientManager.register(Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    assert clientManager.isValid("client1@example.com", "password123")
    assert not clientManager.isValid("cl@example.com", "password123")
    assert not clientManager.isValid("client1@example.com", "password")
    assert not clientManager.isValid("cl@example.com", "password")
    silentRemove("clientTest4.db")

def test_getByEmailAndPassword():
    silentRemove("clientTest5.db")
    clientManager = ClientsManager("clientTest5.db")
    clientManager.register(Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    client = clientManager.getByEmailAndPassword("client1@example.com", "password123")
    assert client == Clients(1, "Client 1", "client1@example.com", "password123", "Company A", "123456789")
    assert clientManager.getByEmailAndPassword("client2@example.com", "password") == None
    silentRemove("clientTest5.db")

def test_getByID():
    silentRemove("clientTest6.db")
    clientManager = ClientsManager("clientTest6.db")
    clientManager.register(Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    client = clientManager.getByID(1)
    assert client == Clients(1, "Client 1", "client1@example.com", "password123", "Company A", "123456789")
    assert clientManager.getByID(2) == None
    silentRemove("clientTest6.db")

def test_getAllIds():
    silentRemove("clientTest7.db")
    clientManager = ClientsManager("clientTest7.db")
    clientManager.register(Clients(1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    clientManager.register(Clients(2, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789'))
    ids = clientManager.getAllIds()
    assert ids == [1, 2]
    silentRemove("clientTest7.db")