import pytest
import os
import sqlite3
from Users import *
from dataclasses import asdict

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "usersTest.db"

@pytest.fixture(scope="module")
def usersManager():
    silentRemove(databaseName)
    userManager = UsersManager(databaseName)
    userManager.register(Users('User 1', 'user1@example.com', 'password123', 'Manager'))
    yield userManager
    silentRemove(databaseName)

def test_createUser():
    user = Users('User 1', 'user1@example.com', 'password123', 'Manager')
    data = asdict(user)
    assert data == {'name': "User 1", 'email': "user1@example.com", 'password': "password123", 'position': "Manager"}

def test_register(usersManager):
    usersManager.register(Users('User 2', 'user2@example.com', 'password123', 'Manager'))
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = 2''')
        assert cursor.fetchone() == (2, 'User 2', 'user2@example.com', 'password123', 'Manager')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_update(usersManager):
    newUser = Users('User Updated', 'updated@example.com', 'newpassword', 'Employee')
    usersManager.update(1, newUser)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'User Updated', 'updated@example.com', 'newpassword', 'Employee')
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_delete(usersManager):
    userID = 1
    usersManager.delete(userID)
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = 1''')
        assert cursor.fetchone() is None
    except:
        assert False
    finally:
        if conn:
            conn.close()

def test_isValid(usersManager):
    assert usersManager.isValid("user1@example.com", "password123")
    assert not usersManager.isValid("us@example.com", "password123")
    assert not usersManager.isValid("user1@example.com", "password")
    assert not usersManager.isValid("us@example.com", "password")

def test_getByEmailAndPassword(usersManager):
    user = usersManager.getByEmailAndPassword("user1@example.com", "password123")
    assert user == Users("User 1", "user1@example.com", "password123", "Manager")
    assert usersManager.getByEmailAndPassword("user2@example.com", "password") == Users(None, None, None, None)