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

openingDate = str(datetime.datetime.now())

def test_createCall():
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    assert call.id == 1
    assert call.title == 'Call 1'
    assert call.description == 'Description 1'
    assert call.category == 'Category 1'
    assert call.clientID == 1
    assert call.userID == 1
    assert call.status == 'open'
    assert call.openingDate == openingDate
    assert call.closingDate == ''
    assert call.maxDate == ''
    assert call.feedback == 'No feedback'

def test_open():
    silentRemove("callsTest1.db")
    callsManager = CallsManager("callsTest1.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    conn = None
    try:
        conn = sqlite3.connect("callsTest1.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Call WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("callsTest1.db")

def test_assignUser():
    silentRemove("callsTest2.db")
    callsManager = CallsManager("callsTest2.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    callsManager.assignUser(1, 2)
    conn = None
    try:
        conn = sqlite3.connect("callsTest2.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Call WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Call 1', 'Description 1', 'Category 1', 1, 2, 'open', openingDate, '', '', 'No feedback')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("callsTest2.db")

def test_changeStatus():
    silentRemove("callsTest3.db")
    callsManager = CallsManager("callsTest3.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    callsManager.changeStatus(1, 'in progress')
    conn = None
    try:
        conn = sqlite3.connect("callsTest3.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Call WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'in progress', openingDate, '', '', 'No feedback')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("callsTest3.db")

def test_close():
    silentRemove("callsTest4.db")
    callsManager = CallsManager("callsTest4.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    callsManager.close(1)
    data = callsManager.DAO.read(1)
    assert data['status'] == 'closed'
    assert data['closingDate'] != ''
    silentRemove("callsTest4.db")

def test_update():
    silentRemove("callsTest5.db")
    callsManager = CallsManager("callsTest5.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    newCall = Calls(1, 'Call Updated', 'Updated Description', 'Updated Category', 1, 1, 'open', openingDate, '', '', 'New feedback')
    callsManager.update(newCall)
    data = callsManager.DAO.read(1)
    assert data['title'] == 'Call Updated'
    assert data['description'] == 'Updated Description'
    assert data['category'] == 'Updated Category'
    assert data['feedback'] == 'New feedback'
    silentRemove("callsTest5.db")

def test_getByID():
    silentRemove("callsTest6.db")
    callsManager = CallsManager("callsTest6.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    data = callsManager.getByID(1)
    assert data == call
    silentRemove("callsTest6.db")

def test_deleteCall():
    silentRemove("callsTest7.db")
    callsManager = CallsManager("callsTest7.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    data = callsManager.DAO.read(1)
    assert data != {}
    callsManager.delete(1)
    data = callsManager.DAO.read(1)
    assert data == {}
    silentRemove("callsTest7.db")

def test_getAllIds():
    silentRemove("callsTest8.db")
    callsManager = CallsManager("callsTest8.db")
    call = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    call2 = Calls(1, 'Call 1', 'Description 1', 'Category 1', 1, 1, 'open', openingDate, '', '', 'No feedback')
    callsManager.open(call)
    callsManager.open(call2)
    ids = callsManager.getAllIds()
    assert ids == [1, 2]
    silentRemove("callsTest8.db")