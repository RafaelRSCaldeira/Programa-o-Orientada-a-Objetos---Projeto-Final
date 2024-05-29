import pytest
import os
import sqlite3
from Database import CallsDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

def test_create():
    silentRemove("callsTest1.db")
    callsDAO = CallsDBDAO("callsTest1.db")
    connection = sqlite3.connect("callsTest1.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info('Call')")
    table_info = cursor.fetchall()
    connection.close()
    assert len(table_info) == 11
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
    assert table_info[10][1] == 'feedback'
    silentRemove("callsTest1.db")

def test_insert():
    silentRemove("callsTest2.db")
    callsDAO = CallsDBDAO("callsTest2.db")
    callData = ['Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29', 'No feedback']
    callsDAO.insert(callData)
    connection = sqlite3.connect("callsTest2.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Call WHERE id = 1")
    data = cursor.fetchone()
    connection.close()
    assert data == (1, 'Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29', 'No feedback')
    silentRemove("callsTest2.db")

def test_read():
    silentRemove("callsTest3.db")
    callsDAO = CallsDBDAO("callsTest3.db")
    callsDAO.insert(['Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29', 'No feedback'])
    callData = callsDAO.read(1)
    assert callData == {'id': 1, 'title': 'Server Issue', 'description': 'Server is down',
                        'category': 'Technical', 'clientID': 1, 'userID': 1, 'status': 'Open',
                        'openingDate': '2024-05-27', 'closingDate': '2024-05-28', 'maxDate': '2024-05-29', 'feedback': 'No feedback'}
    silentRemove("callsTest3.db")

def test_update():
    silentRemove("callsTest4.db")
    callsDAO = CallsDBDAO("callsTest4.db")
    callsDAO.insert(['Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29', 'No feedback'])
    newData = {'title': 'Server Issue Updated', 'description': 'Server is down, hardware issue',
               'category': 'Hardware', 'clientID': 2, 'userID': 2, 'status': 'Closed',
               'openingDate': '2024-05-27', 'closingDate': '2024-05-28', 'maxDate': '2024-05-29', 'feedback': 'We had little problem solving the issue.'}
    callsDAO.update(1, newData)
    callData = callsDAO.read(1)
    assert callData == {'id': 1, 'title': 'Server Issue Updated', 'description': 'Server is down, hardware issue',
                        'category': 'Hardware', 'clientID': 2, 'userID': 2, 'status': 'Closed',
                        'openingDate': '2024-05-27', 'closingDate': '2024-05-28', 'maxDate': '2024-05-29', 'feedback': 'We had little problem solving the issue.'}
    silentRemove("callsTest4.db")

def test_delete():
    silentRemove("callsTest5.db")
    callsDAO = CallsDBDAO("callsTest5.db")
    callsDAO.insert(['Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29', 'No feedback'])
    data = callsDAO.read(1)
    assert data != {}
    callsDAO.delete(1)
    data = callsDAO.read(1)
    assert data == {}
    silentRemove("callsTest5.db")

def test_getAllIds():
    silentRemove("callsTest6.db")
    callsDAO = CallsDBDAO("callsTest6.db")
    callsDAO.insert(['Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29', 'No feedback'])
    callsDAO.insert(['Server Issue', 'Server is down', 'Technical', 1, 1, 'Open', '2024-05-27', '2024-05-28', '2024-05-29', 'No feedback'])
    ids = callsDAO.getAllIds()
    assert ids == [(1,), (2,)]
    silentRemove("callsTest6.db")
