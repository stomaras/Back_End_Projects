'''
Implement a singleton database connection class to mysql database

Prerequisities:
1. Make sure mysql database is installed
2. pip install mysql-connector-python
'''


import mysql.connector
import time

class DatabaseConnection:
    
    __instance = None
    
    @classmethod
    def get_connection(cls):
        if cls.__instance is None:
            DatabaseConnection()
        return cls.__instance
        
    
    def __init__(self):
        if DatabaseConnection.__instance is None:
            raise Exception("Connection already exists")
        else:
            print("Initializing Database Connection...", end=" ")
            self.connection = mysql.connector.connect(host="localhost", database='hrm', user='admin', password='root')
            time.sleep(2)
            print("Established")
            DatabaseConnection.__instance = self
            
    def __str__(self):
        return f"Database Connection: {self.connection}"
    
    
con1 = DatabaseConnection()
con2 = DatabaseConnection()

con1.connection.close()