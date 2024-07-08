# receiver
class Greet:
    def spanish(self):
        print("Hola!")
        
    def english(self):
        print("Hello!")

# Command interface
class Command:
    
    def __init__(self, greeting):
        self._greet = greeting
    
    def execute(self):
        pass
    
# Concrete Command
class HelloCommand(Command):
    def execute(self):
        self._greet.spanish()
        
class HelloCommand2(Command):
    def execute(self):
        self._greet.english()
        
        
# Invoker
class Invoker:
    def __init__(self, commands=[]):
        self.commands = commands
        
    def set_command(self, command):
        self.commands.append(command)
        
    def execute_command(self):
        for command in self.commands:
            command.execute()
        
        
# Client 
# each command called a receiver and each command executed by invoker

greet = Greet()

hello_command = HelloCommand(greet)
hello2 = HelloCommand2(greet)
invoker = Invoker()
invoker.set_command(hello_command)
invoker.set_command(hello2)
invoker.execute_command()