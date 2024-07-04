from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor
        
    @abstractmethod
    def request_handler(self, request):
        pass
    
    
class ConcreteHandler(Handler):
    def request_handler(self, request):
        if request == 'A':
            print(f"{request} is handled at Handler 1")
        elif self.successor is not None:
            print("Handler 1 is not handling this request")
            self.successor.request_handler(request)
            
class ConcreteHandler2(Handler):
    def request_handler(self, request):
        if request == 'B':
            print(f"{request} is handled at Handler 2")
        elif self.successor is not None:
            print("Handler 2 is not handling this request")
            self.successor.request_handler(request)    
        
        
class ConcreteHandler3(Handler):
    def request_handler(self, request):
        if request == 'C':
            print(f"{request} is handled at Handler 3")
        elif self.successor is not None:
            print("Handler 3 is not handling this request")
            self.successor.request_handler(request)
        else:
            print("No handler can handle this request")
            
            
handler1 = ConcreteHandler()
handler2 = ConcreteHandler2()
handler3 = ConcreteHandler3()

handler1.successor = handler2
handler2.successor = handler3

handler1.request_handler('C')