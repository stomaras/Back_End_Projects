from abc import ABC, abstractmethod

#Receiver
class BankAccount:
    def __init__(self,account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
            
    def display_balance(self):
        print(f"Account {self.account_number}, Balance: ${self.balance}")

#####################################
#Command
class Command:
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass
    
class DepositCommand(Command):
    def __init__(self, bank_account, amount):
        self.bank_account = bank_account
        self.amount = amount
        
    def execute(self):
        self.bank_account.deposit(self.amount)
        
    def undo(self):
        self.bank_account.withdraw(self.amount)
        
class WithdrawCommand(Command):
    def __init__(self, bank_account, amount):
        self.bank_account = bank_account
        self.amount = amount
        
    def execute(self):
        self.bank_account.withdraw(self.amount)
        
    def undo(self):
        self.bank_account.deposit(self.amount)
        

##################################
#Invoker

class TransactionManager:
    def __init__(self):
        self.commands = []
        
    def execute_command(self, command):
        command.execute()
        self.commands.append(command)
        
    def undo_last_command(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()
            
            
# client
account = BankAccount("1234567", 1000.0)
transaction_manager = TransactionManager()

transaction_manager.execute_command(DepositCommand(account, 100.0))
transaction_manager.execute_command(WithdrawCommand(account, 10.0))
account.display_balance()




###################################
#client