import pytest
import os
import sqlite3
from Database import ProblemsDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "problemsTest.db"

@pytest.fixture(scope="module")
def problemsDAO():
    silentRemove(databaseName)
    problemsDAO = ProblemsDBDAO(databaseName)
    problemData = [1, '2 hours', 'Server down']
    problemsDAO.insert(problemData)
    yield problemsDAO
    silentRemove(databaseName)

def test_create(problemsDAO):
    problemsDAO.create()
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info('Problem')")
    table_info = cursor.fetchall()
    connection.close()
    assert len(table_info) == 3
    assert table_info[0][1] == 'id'
    assert table_info[1][1] == 'sla'
    assert table_info[2][1] == 'description'

def test_insert(problemsDAO):
    problemData = [2, '1 hour', 'Network issue']
    problemsDAO.insert(problemData)
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Problem WHERE id = 2")
    data = cursor.fetchone()
    connection.close()
    assert data == tuple(problemData)

def test_read(problemsDAO):
    problemID = 1
    problemData = problemsDAO.read(problemID)
    assert problemData == {'id': 1, 'sla': "2 hours", 'description': "Server down"}

def test_update(problemsDAO):
    problemID = 1
    newData = {'sla': '3 hours', 'description': 'Server down, hardware issue'}
    problemsDAO.update(problemID, newData)
    problemData = problemsDAO.read(problemID)
    assert problemData == {'id': 1, 'sla': '3 hours', 'description': 'Server down, hardware issue'}

def test_delete(problemsDAO):
    problemID = 1
    problemsDAO.delete(problemID)
    data = problemsDAO.read(problemID)
    assert data == {}
