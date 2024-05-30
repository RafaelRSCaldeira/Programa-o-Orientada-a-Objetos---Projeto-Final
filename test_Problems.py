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

def test_createProblem():
    problem = Problems(1, 'Server down', 5)
    data = asdict(problem)
    assert data == {'id': 1, 'description': 'Server down', 'sla': 5}

def test_register():
    silentRemove("problemsTest1.db")
    problemManager = ProblemsManager("problemsTest1.db")
    problemManager.register(Problems(1, 'Server down', 2))
    conn = None
    try:
        conn = sqlite3.connect("problemsTest1.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Problem WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'Server down', '2')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("problemsTest1.db")

def test_update():
    silentRemove("problemsTest2.db")
    problemManager = ProblemsManager("problemsTest2.db")
    problemManager.register(Problems(1, 'Server down', 2))
    newProblem = Problems(1, 'License Expired', 1)
    problemManager.update(newProblem)
    conn = None
    try:
        conn = sqlite3.connect("problemsTest2.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Problem WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'License Expired', '1')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("problemsTest2.db")

def test_delete():
    silentRemove("problemsTest3.db")
    problemManager = ProblemsManager("problemsTest3.db")
    problemManager.register(Problems(1, 'Server down', 2))
    problemID = 1
    problemManager.delete(problemID)
    conn = None
    try:
        conn = sqlite3.connect("problemsTest3.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Problem WHERE ID = 1''')
        assert cursor.fetchone() is None
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("problemsTest3.db")

def test_getByID():
    silentRemove("problemsTest4.db")
    problem = Problems(1, 'Server down', '2')
    problemManager = ProblemsManager("problemsTest4.db")
    problemManager.register(problem)
    data = problemManager.getByID(1)
    assert data == Problems(1, 'Server down', '2')
    silentRemove("problemsTest4.db")

def test_getAllIds():
    silentRemove("problemsTest5.db")
    problemManager = ProblemsManager("problemsTest5.db")
    problemManager.register(Problems(1, 'Server down', '2'))
    problemManager.register(Problems(2, 'Server down', '2'))
    ids = problemManager.getAllIds()
    assert ids == [1, 2]
    silentRemove("problemsTest5.db")