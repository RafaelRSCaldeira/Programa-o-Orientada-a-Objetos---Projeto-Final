import pytest
import os
import sqlite3
from Database import UsersDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

def test_create():
    silentRemove("usersTest1.db")
    usersDAO = UsersDBDAO("usersTest1.db")
    connection = sqlite3.connect("usersTest1.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info('User')")
    table_info = cursor.fetchall()
    connection.close()
    assert len(table_info) == 5
    assert table_info[0][1] == 'id'
    assert table_info[1][1] == 'name'
    assert table_info[2][1] == 'email'
    assert table_info[3][1] == 'password'
    assert table_info[4][1] == 'position'
    silentRemove("usersTest1.db")

def test_insert():
    silentRemove("usersTest2.db")
    usersDAO = UsersDBDAO("usersTest2.db")
    userData = ['User 1', 'user1@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    connection = sqlite3.connect("usersTest2.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User WHERE id = 1")
    data = cursor.fetchone()
    connection.close()
    assert data == (1, 'User 1', 'user1@example.com', 'password123', 'Manager')
    silentRemove("usersTest2.db")

def test_read():
    silentRemove("usersTest3.db")
    usersDAO = UsersDBDAO("usersTest3.db")
    userData = ['User 1', 'user1@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    userData = usersDAO.read(1)
    assert userData == {'id': 1, 'name': "User 1", 'email': "user1@example.com", 'password': "password123", 'position': "Manager"}
    silentRemove("usersTest3.db")

def test_update():
    silentRemove("usersTest4.db")
    usersDAO = UsersDBDAO("usersTest4.db")
    userData = ['User 1', 'user1@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    newData = {'name': 'User Updated', 'email': 'updated@example.com', 'password': 'newpassword', 'position': 'Employee'}
    usersDAO.update(1, newData)
    userData = usersDAO.read(1)
    assert userData == {'id': 1, 'name': 'User Updated', 'email': 'updated@example.com', 'password': 'newpassword', 'position': 'Employee'}
    silentRemove("usersTest4.db")

def test_delete():
    silentRemove("usersTest5.db")
    usersDAO = UsersDBDAO("usersTest5.db")
    userData = ['User 1', 'user1@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    data = usersDAO.read(1)
    assert data != {}
    usersDAO.delete(1)
    data = usersDAO.read(1)
    assert data == {}
    silentRemove("usersTest5.db")

def test_getUserByEmailAndPassword():
    silentRemove("usersTest6.db")
    usersDAO = UsersDBDAO("usersTest6.db")
    userData = ['User 1', 'user1@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    userEmail = 'user1@example.com'
    userPassword = 'password123'
    userData = usersDAO.getUserByEmailAndPassword(userEmail, userPassword)
    assert userData == {'id': 1, 'name': "User 1", 'email': "user1@example.com", 'password': "password123", 'position': "Manager"}
    silentRemove("usersTest6.db")

def test_getAllIds():
    silentRemove("usersTest7.db")
    usersDAO = UsersDBDAO("usersTest7.db")
    userData = ['User 1', 'user1@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    usersDAO.insert(userData)
    ids = usersDAO.getAllIds()
    assert ids == [(1,), (2,)]
    silentRemove("usersTest7.db")