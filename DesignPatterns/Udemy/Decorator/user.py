from abc import ABC, abstractmethod

class User:
    def __init__(self, username, password, two_factor_pass):
        self.username = username
        self.password = password
        self.two_factor_pass = two_factor_pass
        
class Authenticator(ABC):
    def __init__(self, user):
        self.user = user
        
    @abstractmethod
    def authenticate(self, password):
        pass
    
class PasswordAuthenticator(Authenticator):
    
    def authenticate(self, password):
        if self.user.password == password:
            print(f"User{self.user.username} is authenticated successfully")
            return True
        else:
            print(f"User{self.user.username} is not authenticated successfully")
            return False
        
user = User("user1","pass","pass123")
auth = PasswordAuthenticator(user)
auth.authenticate("pass")