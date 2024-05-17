import sqlite3

class DatabaseConnection:
    def __init__(self,connection):
        self.connection = connection
        
    def query(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params) if params else cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def insert(self,emp):
        return self.query("INSERT INTO employee VALUES(?,?,?)",(emp.firstname,emp.lastname,emp.age))
    
    def release(self):
        self.connection.rollback()
        
class Employee:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
class DatabaseConnectionPoolManager:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.available_connections = []
        self.in_use_connections = []
        
        self.connection = self.initialize_connection_and_db()
        
        for _ in range(self.max_connections):
            self.available_connections.append(DatabaseConnection(self.connection))
            
    def initialize_connection_and_db(self):
            connection = sqlite3.connect(":memory:")
            cursor = connection.cursor()
            # create employee Table
            cursor.execute("""CREATE TABLE employee (firstname TEXT, lastname TEXT, age INTEGER)""")
            # populates the employees table with lists of Employee data
            employees = [
                Employee(firstname="Oladele", lastname="Ayodeji", age=32),
                Employee(firstname="Oluwaseun", lastname="Bakare", age=50),
                Employee(firstname="Martins",lastname="Floyd", age=14)
            ]
            
            for emp in employees:
                cursor.execute("INSERT INTO employee VALUES(?,?,?)",(emp.firstname,emp.lastname,emp.age))
                
            # close the cursor, commit the changes and return the connection
            cursor.close()
            connection.commit()
            return connection
    
    def acquire_connection(self):
        if self.available_connections:
            dbconnection = self.available_connections.pop()
            self.in_use_connections.append(dbconnection)
            return dbconnection
        else:
            raise Exception("No connections available in the pool.")
        
    def release_connection(self, connection):
        connection.release()
        self.in_use_connections.remove(connection)
        self.available_connections.append(connection)
        
pool = DatabaseConnectionPoolManager(3)

conn1 = pool.acquire_connection()
conn2 = pool.acquire_connection()

query1 = "SELECT * FROM employee"
query2 = "SELECT * FROM employee WHERE age < 50"
result1 = conn1.query(query1)
result2 = conn2.query(query2)

print(f"\nQUERY:{query1}\nRESULT:{result1}")
print(f"\nQUERY:{query2}\nRESULT:{result2}")