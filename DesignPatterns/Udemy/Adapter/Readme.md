# Target: This is the interface that the client code uses to interact with the system.
# The Target defines the methods that the client code can call to achieve the desired functionality.

# Adaptee: This is the existing system that needs to be adapted to work with the Targer Interface. The Adaptee has a different
# interface than the Target, and the client code cannot use the Adaptee interface

# Adapter: This is the class that adapts the Adaptee to the target interface. The Adapter implements the Target interface and uses 
# an instance of the Adaptee interface to provide the desired functionality

# Client Code: This is the code that uses the Target interface to interact with the system. The client code is unaware of the 
# Adaptee interface and the Adapter, and only interact with the Targert Interface