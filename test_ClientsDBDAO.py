import pytest
import os
import sqlite3
from Database import ClientsDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "clientsTest.db"

@pytest.fixture(scope="module")
def clientsDAO():
    silentRemove(databaseName)
    clientsDAO = ClientsDBDAO(databaseName)
    clientData = ['Client 1', 'client1@example.com', 'password123', 'Company A', '123456789']
    clientsDAO.insert(clientData)
    yield clientsDAO
    silentRemove(databaseName)

def test_create(clientsDAO):
    clientsDAO.create()
    connection = sqlite3.connect(databaseName)
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

def test_insert(clientsDAO):
    clientData = ['Client 2', 'client2@example.com', 'password321', 'Company B', '987654321']
    clientsDAO.insert(clientData)
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Client WHERE id = 2")
    data = cursor.fetchone()
    connection.close()
    assert data == (2, 'Client 2', 'client2@example.com', 'password321', 'Company B', '987654321')

def test_read(clientsDAO):
    clientID = 1
    clientData = clientsDAO.read(clientID)
    assert clientData == {'id': 1, 'name': "Client 1", 'email': "client1@example.com", 'password': "password123", 'company': "Company A", 'phone': "123456789"}

def test_update(clientsDAO):
    clientID = 1
    newData = {'name': 'Client Updated', 'email': 'updatedclient@example.com', 'password': 'newpassword', 'company': 'New Company', 'phone': '987654321'}
    clientsDAO.update(clientID, newData)
    clientData = clientsDAO.read(clientID)
    assert clientData == {'id': 1, 'name': 'Client Updated', 'email': 'updatedclient@example.com', 'password': 'newpassword', 'company': 'New Company', 'phone': '987654321'}

def test_delete(clientsDAO):
    clientID = 1
    clientsDAO.delete(clientID)
    data = clientsDAO.read(clientID)
    assert data == {}

