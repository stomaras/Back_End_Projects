from abc import ABC, abstractmethod

# Remote service interface
class RemoteService(ABC):
    @abstractmethod
    def perform_action(self):
        pass
    
# Real remote service implementation
class RemoteServiceImpl(RemoteService):
    def perform_action(self):
        print("Performing action on the remote service")
        # perform other remote actions.
        
class RemoteServiceProxy(RemoteService):
    def __init__(self, remote_service):
        self.remote_service = remote_service
        
    def perform_action(self):
        print("Proxy: Before performing action")
        self.remote_service.perform_action()
        print("Proxy: After performing action")
        
        
# usage
remote_service = RemoteServiceImpl()
proxy = RemoteServiceProxy(remote_service)

# remote_service.perform_action()
proxy.perform_action()