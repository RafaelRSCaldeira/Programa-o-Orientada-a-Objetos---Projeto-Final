import pytest
import os
import sqlite3
from Problems import *
from dataclasses import asdict

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "problemsTest.db"

@pytest.fixture(scope="module")
def problemsManager():
    silentRemove(databaseName)
    problemManager = ProblemsManager(databaseName)
    problemManager.register(Problems('Server down', 2))
    yield problemManager
    silentRemove(databaseName)

def test_createProblem():
    problem = Problems('Server down', 5)
    data = asdict(problem)
    assert data == {'description': 'Server down', 'sla': 5}

def test_register(problemsManager):
    problemsManager.register(Problems('Server down', 2))
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Problem WHERE ID = 2''')
        assert cursor.fetchone() == (2, '2', 'Server down')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_update(problemsManager):
    newProblem = Problems('License Expired', 1)
    problemsManager.update(1, newProblem)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Problem WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'License Expired', '1')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_delete(problemsManager):
    problemID = 1
    problemsManager.delete(problemID)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Problem WHERE ID = 1''')
        assert cursor.fetchone() is None
    except:
        assert False
    finally:
        if conn:
            conn.close()