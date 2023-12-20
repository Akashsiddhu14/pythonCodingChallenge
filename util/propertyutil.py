import configparser


class PropertyUtil:
    @staticmethod
    def getPropertyString():

        connection_params = {
            'host': 'localhost',
            'database': 'insurance',
            'user': 'root',
            'password': 'akash1436',
            'port': '3306'
        }
        return connection_params
