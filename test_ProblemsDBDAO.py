import pytest
import os
import sqlite3
from Database import ProblemsDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

def test_create():
    silentRemove("problemsTest1.db")
    problemsDAO = ProblemsDBDAO("problemsTest1.db")
    connection = sqlite3.connect("problemsTest1.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info('Problem')")
    table_info = cursor.fetchall()
    connection.close()
    assert len(table_info) == 3
    assert table_info[0][1] == 'id'
    assert table_info[1][1] == 'description'
    assert table_info[2][1] == 'sla'
    silentRemove("problemsTest1.db")

def test_insert():
    silentRemove("problemsTest2.db")
    problemsDAO = ProblemsDBDAO("problemsTest2.db")
    problemData = ['Server down', '2 hours']
    problemsDAO.insert(problemData)
    connection = sqlite3.connect("problemsTest2.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Problem WHERE id = 1")
    data = cursor.fetchone()
    connection.close()
    assert data == (1, 'Server down', '2 hours')
    silentRemove("problemsTest2.db")

def test_read():
    silentRemove("problemsTest3.db")
    problemsDAO = ProblemsDBDAO("problemsTest3.db")
    problemData = ['Server down', '2 hours']
    problemsDAO.insert(problemData)
    problemID = 1
    problemData = problemsDAO.read(problemID)
    assert problemData == {'id': 1, 'sla': "2 hours", 'description': "Server down"}
    silentRemove("problemsTest3.db")

def test_update():
    silentRemove("problemsTest4.db")
    problemsDAO = ProblemsDBDAO("problemsTest4.db")
    problemData = ['Server down', '2 hours']
    problemsDAO.insert(problemData)
    newData = {'sla': '3 hours', 'description': 'Server down, hardware issue'}
    problemsDAO.update(1, newData)
    problemData = problemsDAO.read(1)
    assert problemData == {'id': 1, 'sla': '3 hours', 'description': 'Server down, hardware issue'}
    silentRemove("problemsTest4.db")

def test_delete():
    silentRemove("problemsTest5.db")
    problemsDAO = ProblemsDBDAO("problemsTest5.db")
    problemData = ['Server down', '2 hours']
    problemsDAO.insert(problemData)
    data = problemsDAO.read(1)
    assert data != {}
    problemsDAO.delete(1)
    data = problemsDAO.read(1)
    assert data == {}
    silentRemove("problemsTest5.db")

def test_getAllIds():
    silentRemove("problemsTest6.db")
    problemsDAO = ProblemsDBDAO("problemsTest6.db")
    problemData = ['Server down', '2 hours']
    problemsDAO.insert(problemData)
    problemsDAO.insert(problemData)
    ids = problemsDAO.getAllIds()
    assert ids == [(1,), (2,)]
    silentRemove("problemsTest6.db")
