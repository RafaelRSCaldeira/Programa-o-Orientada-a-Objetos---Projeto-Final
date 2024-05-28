import pytest
import os
import sqlite3
from Database import UsersDBDAO

def silentRemove(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass

databaseName = "usersTest.db"

@pytest.fixture(scope="module")
def usersDAO():
    silentRemove(databaseName)
    usersDAO = UsersDBDAO(databaseName)
    userData = ['User 1', 'user1@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    yield usersDAO
    silentRemove(databaseName)

def test_create(usersDAO):
    usersDAO.create()
    connection = sqlite3.connect(databaseName)
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

def test_insert(usersDAO):
    userData = ['User 2', 'user2@example.com', 'password123', 'Manager']
    usersDAO.insert(userData)
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User WHERE id = 2")
    data = cursor.fetchone()
    connection.close()
    assert data == (2, 'User 2', 'user2@example.com', 'password123', 'Manager')

def test_read(usersDAO):
    userID = 1
    userData = usersDAO.read(userID)
    assert userData == {'id': 1, 'name': "User 1", 'email': "user1@example.com", 'password': "password123", 'position': "Manager"}

def test_update(usersDAO):
    userID = 1
    newData = {'name': 'User Updated', 'email': 'updated@example.com', 'password': 'newpassword', 'position': 'Employee'}
    usersDAO.update(userID, newData)
    userData = usersDAO.read(userID)
    assert userData == {'id': 1, 'name': 'User Updated', 'email': 'updated@example.com', 'password': 'newpassword', 'position': 'Employee'}

def test_delete(usersDAO):
    userID = 1
    usersDAO.delete(userID)
    data = usersDAO.read(userID)
    assert data == {}

def test_getUserByEmailAndPassword(usersDAO):
    userEmail = 'user1@example.com'
    userPassword = 'password123'
    userData = usersDAO.getUserByEmailAndPassword(userEmail, userPassword)
    assert userData == {'id': 1, 'name': "User 1", 'email': "user1@example.com", 'password': "password123", 'position': "Manager"}
