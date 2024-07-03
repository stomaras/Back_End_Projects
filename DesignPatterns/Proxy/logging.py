from abc import ABC, abstractmethod
from datetime import datetime


class DatabaseQuery(ABC):
    @abstractmethod
    def execute(self, query):
        pass 
    
class RealDatabaseQuery(DatabaseQuery):
    def execute(self, query):
        return f"Result for query '{query}'"
    
class LoggingProxyDatabaseQuery(DatabaseQuery):
    def __init__(self, database_query):
        self.database_query = database_query
        
    def execute(self, query):
        print(f"Executing query '{query}...")
        result = self.database_query.execute(query)
        # log
        self.log_to_file(f"{datetime.now()} {result}\n")
        return result
    
    def log_to_file(self, message):
        with open("querylog.txt",'a') as logfile:
            logfile.write(message)
            
            
# Client Code
real_query = RealDatabaseQuery()
logged_query = LoggingProxyDatabaseQuery(real_query)


print(logged_query.execute("SELECT * FROM users"))