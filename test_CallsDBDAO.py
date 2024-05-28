import pytest
import os
import sqlite3
from Database import CallsDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "callsTest.db"

@pytest.fixture(scope="module")
def callsDAO():
    silentRemove(databaseName)
    callsDAO = CallsDBDAO(databaseName)
    callData = ['Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29']
    callsDAO.insert(callData)
    yield callsDAO
    silentRemove(databaseName)

def test_create(callsDAO):
    callsDAO.create()
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info('Call')")
    table_info = cursor.fetchall()
    connection.close()
    assert len(table_info) == 10
    assert table_info[0][1] == 'id'
    assert table_info[1][1] == 'title'
    assert table_info[2][1] == 'description'
    assert table_info[3][1] == 'category'
    assert table_info[4][1] == 'clientID'
    assert table_info[5][1] == 'userID'
    assert table_info[6][1] == 'status'
    assert table_info[7][1] == 'openingDate'
    assert table_info[8][1] == 'closingDate'
    assert table_info[9][1] == 'maxDate'

def test_insert(callsDAO):
    callData = ['Network Issue', 'Network is slow', 'Technical', 2, 2, 'Open', '2024-05-27', '2024-05-28', '2024-05-29']
    callsDAO.insert(callData)
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Call WHERE id = 2")
    data = cursor.fetchone()
    connection.close()
    assert data == (2, 'Network Issue', 'Network is slow', 'Technical', 2, 2, 'Open', '2024-05-27', '2024-05-28', '2024-05-29')

def test_read(callsDAO):
    callID = 1
    callData = callsDAO.read(callID)
    assert callData == {'id': 1, 'title': 'Server Issue', 'description': 'Server is down',
                        'category': 'Technical', 'clientID': 1, 'userID': 1, 'status': 'Open',
                        'openingDate': '2024-05-27', 'closingDate': '2024-05-28', 'maxDate': '2024-05-29'}

def test_update(callsDAO):
    callID = 1
    newData = {'title': 'Server Issue Updated', 'description': 'Server is down, hardware issue',
               'category': 'Hardware', 'clientID': 2, 'userID': 2, 'status': 'Closed',
               'openingDate': '2024-05-27', 'closingDate': '2024-05-28', 'maxDate': '2024-05-29'}
    callsDAO.update(callID, newData)
    callData = callsDAO.read(callID)
    assert callData == {'id': 1, 'title': 'Server Issue Updated', 'description': 'Server is down, hardware issue',
                        'category': 'Hardware', 'clientID': 2, 'userID': 2, 'status': 'Closed',
                        'openingDate': '2024-05-27', 'closingDate': '2024-05-28', 'maxDate': '2024-05-29'}

def test_delete(callsDAO):
    callID = 1
    callsDAO.delete(callID)
    data = callsDAO.read(callID)
    assert data == {}
