from abc import ABC, abstractmethod

# Database Connection
class Connection(ABC):
    
    @abstractmethod
    def connect(self):
        pass

class MySQLConnection(Connection):
    def connect(self):
        print("Connecting to MySQL")

class OracleConnection(Connection):
    def connect(self):
        print("Connecting to Oracle")
        
class PostgreSQLConnection(Connection):
    def connect(self):
        print("Connecting to PostgreSQL")

# Database cursor
class Cursor(ABC):
    @abstractmethod
    def execute(self, query:str):
        pass
    
class MySQLCursor(Cursor):
    def execute(self, query:str):
        print(f"Executing MySQL query '{query}' on MySQL")

class PostgreCursor(Cursor):
    def execute(self, query:str):
        print(f"Executing PostgreSQL query '{query}' on PostgreSQL")    
    
class OracleCursor(Cursor):
    def execute(self, query:str):
        print(f"Executing Oracle query '{query}' on Oracle")
    
# Factory for generating Connection and Cursor for specific database
class AbstractDBFactory(ABC):
    
    @abstractmethod
    def create_connection(self):
        pass
    
    @abstractmethod
    def create_cursor(self):
        pass
    
class MySQLDBFactory(AbstractDBFactory):
    
    def create_connection(self):
        return MySQLConnection()
    
    def create_cursor(self):
        return MySQLCursor()
    
class OracleDBFactory(AbstractDBFactory):
    
    def create_connection(self):
        return OracleConnection()
    
    def create_cursor(self):
        return OracleCursor()
    
def client():
    factories = dict(mysql=MySQLDBFactory, oracle=OracleDBFactory)
    
    fact_list = ",".join(factories)
    print(fact_list)
    
    while True:
        db = input(f"Enter database name:{fact_list}: ")
        
        if db in factories:
            break
        print('This database does not exist - try again...({fact_list})')
        
    return factories.get(db)()

if __name__ == '__main__':
    db_factory = client()
    db_connect = db_factory.create_connection()
    cursor = db_factory.create_cursor()
    
    db_connect.connect()
    cursor.execute("SELECT * FROM STUDENT")
    
client()