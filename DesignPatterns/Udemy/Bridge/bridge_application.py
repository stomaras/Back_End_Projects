# Build a web application abstraction that has these functions 1.Route URL 2.Render template 3.Execute Database queries.
# Our task is to decouple the 3rd function of the application (Execute database query) to a Database Driver Abstract class that enables
# you to create different type of database implementation for the application.
# The database driver should handle 1. connection 2. running of query 3.disconnection
from abc import ABC, abstractmethod
#================Abstraction===========================
#(Abstract Class) - Web Application Prototype
class WebApplicationFramework(ABC):
    def __init__(self, db_driver):
        self.db_driver = db_driver

    @abstractmethod
    def route(self,path):
        pass
    
    @abstractmethod
    def render_template(self,template):
        pass
    
    def execute_query(self,query):
        self.db_driver.connect()
        self.db_driver.execute(query)
        self.db_driver.disconnect()

#==================Refinning Abstraction========================
#(Concrete Abstraction) Web Application Samples - eg Flask, Django, etc

class Flask(WebApplicationFramework):
    def route(self,path):
        print(f"Routing to {path} using Flask...")
        
    def render_template(self,template):
        print(f"Rendering template {template} using Flask...")
        
    
class Django(WebApplicationFramework):
    def route(self,path):
        print(f"Routing to {path} using Django...")
        
    def render_template(self,template):
        print(f"Rendering template {template} using Django...")

###########################################################################################################

#=========================Implementation=========================
# Database Driver Abstract Class
class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute(self,query):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

#===============Concrete Implementation================
# Database Driver Examples -eg. MySQLDriver, PostgresDriver, etc

class MySQLDriver(DatabaseDriver):
    def connect(self):
        print("Connecting to MySQL...")
        
    def execute(self,query):
        print(f"Executing MySQL query '{query}'...")
        
    def disconnect(self):
        print("Disconnecting from MySQL...")
        
class PostgresDriver(DatabaseDriver):
    def connect(self):
        print("Connecting to PostgreSQL...")
        
    def execute(self,query):
        print(f"Executing PostgreSQL query '{query}'...")
        
    def disconnect(self):
        print("Disconnecting from PostgreSQL...")
        
        
if __name__ == '__main__':
    flask = Flask(MySQLDriver())
    flask.route('/')
    flask.render_template('index.html')
    flask.execute_query('SELECT * FROM users')
    print("===============================================\n")
    django = Django(PostgresDriver())
    django.route('/')
    django.render_template('index.html')
    django.execute_query('SELECT * FROM users')
    
    
    
    
    
    