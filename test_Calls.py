import pytest
import os
import sqlite3
import datetime
from Calls import *

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "callsTest.db"
opening_date = str(datetime.datetime.now())

@pytest.fixture(scope="module")
def callsManager():
    silentRemove(databaseName)
    manager = CallsManager(databaseName)
    call = Calls('Call 1', 'Description 1', 'Category 1', 1, 1, 'open', opening_date, '', '')
    manager.open(call)
    yield manager
    silentRemove(databaseName)

def test_createCall():
    call = Calls('Call 1', 'Description 1', 'Category 1', 1, 1, 'open', opening_date, '', '')
    assert call.title == 'Call 1'
    assert call.description == 'Description 1'
    assert call.category == 'Category 1'
    assert call.clientID == 1
    assert call.userID == 1
    assert call.status == 'open'
    assert call.openingDate == opening_date
    assert call.closingDate == ''
    assert call.maxDate == ''

def test_open(callsManager):
    call = Calls('Call 2', 'Description 2', 'Category 2', 2, 2, 'open', opening_date, '', '')
    callsManager.open(call)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Call WHERE ID = 2''')
        assert cursor.fetchone() == (2, 'Call 2', 'Description 2', 'Category 2', 2, 2, 'open', opening_date, '', '')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_assignUser(callsManager):
    callsManager.assignUser(1, 2)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Call WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Call 1', 'Description 1', 'Category 1', 1, 2, 'open', opening_date, '', '')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_changeStatus(callsManager):
    callsManager.changeStatus(1, 'in progress')
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Call WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'in progress', opening_date, '', '')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_closeCall(callsManager):
    callsManager.close(1)
    data = callsManager.DAO.read(1)
    assert data['status'] == 'closed'
    assert data['closingDate'] != ''

def test_updateCall(callsManager):
    new_data = {'title': 'Call Updated', 'description': 'Updated Description', 'category': 'Updated Category'}
    callsManager.update(1, new_data)
    data = callsManager.DAO.read(1)
    assert data['title'] == 'Call Updated'
    assert data['description'] == 'Updated Description'
    assert data['category'] == 'Updated Category'

def test_deleteCall(callsManager):
    callsManager.delete(1)
    data = callsManager.DAO.read(1)
    assert data == {}