import pytest
import os
import sqlite3
from Database import ClientsDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

def test_create():
    silentRemove("clientsTest1.db")
    clientsDAO = ClientsDBDAO("clientsTest1.db")
    connection = sqlite3.connect("clientsTest1.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info('Client')")
    table_info = cursor.fetchall()
    connection.close()
    assert len(table_info) == 6
    assert table_info[0][1] == 'id'
    assert table_info[1][1] == 'name'
    assert table_info[2][1] == 'email'
    assert table_info[3][1] == 'password'
    assert table_info[4][1] == 'company'
    assert table_info[5][1] == 'phone'
    silentRemove("clientsTest1.db")

def test_insert():
    silentRemove("clientsTest2.db")
    clientsDAO = ClientsDBDAO("clientsTest2.db")
    clientData = ['Client 1', 'client1@example.com', 'password123', 'Company A', '123456789']
    clientsDAO.insert(clientData)
    connection = sqlite3.connect("clientsTest2.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Client WHERE id = 1")
    data = cursor.fetchone()
    connection.close()
    assert data == (1, 'Client 1', 'client1@example.com', 'password123', 'Company A', '123456789')
    silentRemove("clientsTest2.db")

def test_read():
    silentRemove("clientsTest3.db")
    clientsDAO = ClientsDBDAO("clientsTest3.db")
    clientData = ['Client 1', 'client1@example.com', 'password123', 'Company A', '123456789']
    clientsDAO.insert(clientData)
    clientData = clientsDAO.read(1)
    assert clientData == {'id': 1, 'name': "Client 1", 'email': "client1@example.com", 'password': "password123", 'company': "Company A", 'phone': "123456789"}
    silentRemove("clientsTest3.db")

def test_update():
    silentRemove("clientsTest4.db")
    clientsDAO = ClientsDBDAO("clientsTest4.db")
    clientData = ['Client 1', 'client1@example.com', 'password123', 'Company A', '123456789']
    clientsDAO.insert(clientData)
    newData = {'name': 'Client Updated', 'email': 'updatedclient@example.com', 'password': 'newpassword', 'company': 'New Company', 'phone': '987654321'}
    clientsDAO.update(1, newData)
    clientData = clientsDAO.read(1)
    assert clientData == {'id': 1, 'name': 'Client Updated', 'email': 'updatedclient@example.com', 'password': 'newpassword', 'company': 'New Company', 'phone': '987654321'}
    silentRemove("clientsTest4.db")

def test_delete():
    silentRemove("clientsTest5.db")
    clientsDAO = ClientsDBDAO("clientsTest5.db")
    clientData = ['Client 1', 'client1@example.com', 'password123', 'Company A', '123456789']
    clientsDAO.insert(clientData)
    data = clientsDAO.read(1)
    assert data != {}
    clientsDAO.delete(1)
    data = clientsDAO.read(1)
    assert data == {}
    silentRemove("clientsTest5.db")

def test_getClientByEmailAndPassword():
    silentRemove("clientsTest6.db")
    clientsDAO = ClientsDBDAO("clientsTest6.db")
    clientData = ['Client 1', 'client1@example.com', 'password123', 'Company A', '123456789']
    clientsDAO.insert(clientData)
    clientEmail = 'client1@example.com'
    clientPassword = 'password123'
    clientData = clientsDAO.getClientByEmailAndPassword(clientEmail, clientPassword)
    assert clientData == {'id': 1, 'name': "Client 1", 'email': "client1@example.com", 'password': "password123", 'company': "Company A", 'phone': "123456789"}
    silentRemove("clientsTest6.db")

def test_getAllIds():
    silentRemove("clientsTest7.db")
    clientsDAO = ClientsDBDAO("clientsTest7.db")
    clientData = ['Client 1', 'client1@example.com', 'password123', 'Company A', '123456789']
    clientsDAO.insert(clientData)
    clientsDAO.insert(clientData)
    ids = clientsDAO.getAllIds()
    assert ids == [(1,), (2,)]
    silentRemove("clientsTest7.db")
