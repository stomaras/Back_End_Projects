from abc import ABC, abstractmethod
from random import randint

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def get_balance(self):
        pass
    
class RealBankAccount(BankAccount):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
            
    def get_balance(self):
        return self.balance
    
class BankAccountProxy(BankAccount):
    def __init__(self):
        self.real_account = None
        self.username = input("Enter username")
        self.password = input("Enter password")
        
    def authenticated(self):
        dbuser_password = self.password_source(self.username)
        
        if dbuser_password == self.password:
            if not self.real_account:
                self.real_account = RealBankAccount(randint(100000, 999999), 0)
                print()
                print("ACCOUNT:", self.real_account.account_number)
                print("="*20)
            return True
        else:
            return ValueError("Authentication Failed")
        
    def deposit(self, amount):
        if self.authenticated():
            self.real_account.deposit(amount)
 
    def withdraw(self, amount):
        if self.authenticated():
            self.real_account.withdraw(amount)
        
    def get_balance(self):
        if self.authenticated():
            return self.real_account.get_balance()
        
    def password_source(self, pwd):
        pwd_list = {
            "user1":"pass1",
            "user2":"pass2",
            "admin":"admin"
        }
        
        return pwd_list.get(pwd)
    
    
account1 = BankAccountProxy()

try:
    to_deposit = 1000
    to_withdraw = 120
    
    account1.deposit(to_deposit)
    print(f"Balance: ${account1.get_balance()}")
    
    print(f"Make Withdrwal of ${to_withdraw}")
    account1.withdraw(to_withdraw)
    print(f"Balance: ${account1.get_balance()}")
    
except ValueError as e:
    print(e)
    