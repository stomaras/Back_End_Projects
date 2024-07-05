from abc import ABC, abstractmethod

class Request:
    def __init__(self, amount):
        self.amount = amount
        
        
# handler interface
class Handler:
    def __init__(self, successor=None):
        self.successor = successor
    
    @abstractmethod
    def handle_request(self, request):
        pass
    
class Manager(Handler):
    def handle_request(self, request):
        if request.amount <= 1000:
            print(f"Manager approved the request for {request.amount}")
        elif self.successor is not None:
            self.successor.handle_request(request)
            
class Director(Handler):
    def handle_request(self, request):
        if request.amount <= 5000:
            print(f"Director approved the request for {request.amount}")
        elif self.successor is not None:
            self.successor.handle_request(request)
            
class CEO(Handler):
    def handle_request(self, request):
        if request.amount <= 10000:
            print(f"CEO approved the request for {request.amount}")
        elif self.successor is not None:
            self.successor.handle_request(request)
        else:
            print(f"Request exceeds the CEO's approval limit")            


handler = Manager(Director(CEO()))
request1 = Request(500)
handler.handle_request(request1)