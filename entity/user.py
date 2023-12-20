import mysql.connector as sql

conn = sql.connect(host='localhost', database='insurance', user='root', password='akash1436')


class User:

    def __init__(self, userId, username, password, role):
        self._userId = userId
        self._username = username
        self._password = password
        self._role = role

    def getUserId(self):
        return self._userId

    def getUsername(self):
        return self._username

    def getPassword(self):
        return self._password

    def getRole(self):
        return self._role

    def setUserId(self, userId):
        self._userId = userId

    def setUsername(self, username):
        self._username = username

    def setPassword(self, password):
        self._password = password

    def setRole(self, role):
        self._role = role