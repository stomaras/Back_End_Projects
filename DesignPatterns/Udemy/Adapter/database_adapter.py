class PostgreSQLDatabase: #Adaptee
    def postgresql_insert(self, data):
        print(f"Inserting {data} into PostgreSQL Database")
        
    def postgresql_update(self, data):
        print(f"Updating {data} into PostgreSQL Database")
        
    def postgresql_delete(self, data):
        print(f"Deleting {data} into PostgreSQL Database")
        
    def postgresql_select(self, data):
        print(f"Selecting {data} from PostgreSQL Database")
        
class MySQLDatabase: #Adaptee
    def mysql_insert(self, data):
        print(f"Inserting {data} into MySQL Database")
        
    def mysql_update(self, data):
        print(f"Updating {data} into MySQL Database")
        
    def mysql_delete(self, data):
        print(f"Deleting {data} into MySQL Database")
        
    def mysql_select(self, data):
        print(f"Selecting {data} from MySQL Database")
        
class Database: #Target
    def insert(self, data):
        pass
    
    def delete(self, data):
        pass
    
    def update(self, data):
        pass
    
    def select(self, data):
        pass
    
class MySQLAdapter(Database):
    def __init__(self, adaptee):
        self.adaptee = adaptee
        
    def insert(self, data):
        self.adaptee.mysql_insert(data)
        
    def delete(self, data):
        self.adaptee.mysql_delete(data)
        
    def update(self, data):
        self.adaptee.mysql_update(data)
        
    def select(self, data):
        self.adaptee.mysql_select(data)
        
class PostgreSQLAdapter(Database):
    def __init__(self, adaptee):
        self.adaptee = adaptee
        
    def insert(self, data):
        self.adaptee.postgresql_insert(data)
        
    def delete(self, data):
        self.adaptee.postgresql_delete(data)
        
    def update(self, data):
        self.adaptee.postgresql_update(data)
        
    def select(self, data):
        self.adaptee.postgresql_select(data)
        
if __name__ == "__main__":
    mysqlAdapter = MySQLAdapter(MySQLDatabase())
    mysqlAdapter.insert("Data")
    mysqlAdapter.delete("Data2")
    mysqlAdapter.update("Data3")
    mysqlAdapter.select("Data4")
    
    
    postgresAdapter = PostgreSQLAdapter(PostgreSQLDatabase())
    postgresAdapter.insert('Record 1')
    postgresAdapter.select('Record 2')
    