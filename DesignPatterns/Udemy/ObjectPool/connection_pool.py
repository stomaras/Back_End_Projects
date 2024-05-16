import random
import time


class Connection:
    def __init__(self, id):
        self.id = id
        self.is_connected = False
        
    def connect(self):
        # Simulate conncetion establishment
        print(f"Connecting to server... Connection ID:{self.id}")
        time.sleep(1)
        self.is_connected = True
        print(f"Connected! Connection ID:{self.id}")
        
    def disconnect(self):
        # Simulate connection termination
        print(f"Disconnecting from server... Connection ID:{self.id}")
        time.sleep(1)
        self.is_connected = False
        print(f"Disconnected! Connection ID:{self.id}")
        
        
class ConnectionPoolManager:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.available_connections = []
        self.in_use_connections = []
        
        
        for i in range(self.max_connections):
            self.available_connections.append(Connection(i))
            
    def acquire_connection(self):
        if self.available_connections:
            conn = self.available_connections.pop()
            self.in_use_connections.append(conn)
            conn.connect()
            return conn
        else:
            raise Exception("No connections available in the pool.")

        
    def release_connection(self, conn):
        conn.disconnect()
        self.in_use_connections.remove(conn)
        self.available_connections.append(conn)
        
if __name__ == "__main__":
    
    pool = ConnectionPoolManager(3)
    
    # Acquire connections from the pool
    conn1 = pool.acquire_connection()
    conn2 = pool.acquire_connection()