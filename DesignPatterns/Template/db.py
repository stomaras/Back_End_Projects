from abc import ABC, abstractmethod

class DatabaseQueryExecutionTemplate(ABC):
    def execute_query(self, query):
        self.connect_to_database()
        result = self.run_query(query)
        self.process_results(result)
        self.disconnect_from_database()
        
    def connect_to_database(self):
        print("Connecting to database...")
        
    @abstractmethod
    def run_query(self, query):
        pass
    
    
    def process_results(self, result):
        print("Processing results...",result)
        
    def disconnect_from_database(self):
        print("Disconnecting from database...")
        
        
class MySQLQueryExecutionTemplate(DatabaseQueryExecutionTemplate):
    def run_query(self, query):
        print(f"Executing MySQL query '{query}'...")
        # Simulate querying data from MySQL
        
class PostgreSQLQueryExecutionTemplate(DatabaseQueryExecutionTemplate):
    def run_query(self, query):
        print(f"Executing PostgreSQL query '{query}'...")
        # Simulate querying data from PostgreSQL
        
        
        
# client

if __name__ == '__main__':
    mysql_query = MySQLQueryExecutionTemplate()
    mysql_query.run_query("SELECT * FROM users")
    
    postgresql_query = PostgreSQLQueryExecutionTemplate()
    postgresql_query.run_query("SELECT * FROM orders")
    