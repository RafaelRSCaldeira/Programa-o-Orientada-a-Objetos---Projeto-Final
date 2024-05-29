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

def test_createUser():
    user = Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager')
    data = asdict(user)
    assert data == {'id': 1, 'name': "User 1", 'email': "user1@example.com", 'password': "password123", 'position': "Manager"}

def test_register():
    silentRemove("usersTest1.db")
    userManager = UsersManager("usersTest1.db")
    userManager.register(Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager'))
    conn = None
    try:
        conn = sqlite3.connect("usersTest1.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'User 1', 'user1@example.com', 'password123', 'Manager')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("usersTest1.db")

def test_update():
    silentRemove("usersTest2.db")
    userManager = UsersManager("usersTest2.db")
    userManager.register(Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager'))
    newUser = Users(1, 'User Updated', 'updated@example.com', 'newpassword', 'Employee')
    userManager.update(newUser)
    conn = None
    try:
        conn = sqlite3.connect("usersTest2.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = 1''')
        assert cursor.fetchone() == (1, 'User Updated', 'updated@example.com', 'newpassword', 'Employee')
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("usersTest2.db")

def test_delete():
    silentRemove("usersTest3.db")
    userManager = UsersManager("usersTest3.db")
    userManager.register(Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager'))
    userID = 1
    userManager.delete(userID)
    conn = None
    try:
        conn = sqlite3.connect("usersTest3.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM User WHERE ID = 1''')
        assert cursor.fetchone() is None
    except:
        assert False
    finally:
        if conn:
            conn.close()
    silentRemove("usersTest3.db")

def test_isValid():
    silentRemove("usersTest4.db")
    userManager = UsersManager("usersTest4.db")
    userManager.register(Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager'))
    assert userManager.isValid("user1@example.com", "password123")
    assert not userManager.isValid("us@example.com", "password123")
    assert not userManager.isValid("user1@example.com", "password")
    assert not userManager.isValid("us@example.com", "password")
    silentRemove("usersTest4.db")

def test_getByEmailAndPassword():
    silentRemove("usersTest5.db")
    userManager = UsersManager("usersTest5.db")
    userManager.register(Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager'))
    user = userManager.getByEmailAndPassword("user1@example.com", "password123")
    assert user == Users(1, "User 1", "user1@example.com", "password123", "Manager")
    assert userManager.getByEmailAndPassword("user2@example.com", "password") is None
    silentRemove("usersTest5.db")

def test_getByID():
    silentRemove("usersTest6.db")
    user = Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager')
    userManager = UsersManager("usersTest6.db")
    userManager.register(user)
    data = userManager.getByID(1)
    assert data == user
    silentRemove("usersTest6.db")

def test_getAllIds():
    silentRemove("usersTest7.db")
    userManager = UsersManager("usersTest7.db")
    userManager.register(Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager'))
    userManager.register(Users(1, 'User 1', 'user1@example.com', 'password123', 'Manager'))
    ids = userManager.getAllIds()
    assert ids == [1, 2]
    silentRemove("usersTest7.db")