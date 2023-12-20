import mysql.connector as sql
import util.propertyutil
from util import propertyutil

class DBConnection:
    _connection = None

    @staticmethod
    def getConnection():
        object = propertyutil.PropertyUtil()

        if DBConnection._connection is None:
            connection_string = object.getPropertyString()
            'DBConnection._connection = sql.connect(**connection_string)'''

            DBConnection._connection = sql.connect(host='localhost', database='insurance', user='root', password='akash1436')
            if DBConnection._connection.is_connected():
                print("Database connection is successful")
            return DBConnection._connection
