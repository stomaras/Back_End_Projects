from abc import ABC, abstractmethod

#Receiver
class TV:
    def turn_on(self):
        print("TV is turned on")
        
    def turn_off(self):
        print("TV is turned off")
        
# Command interface
class Command(ABC):
    def __init__(self, tv):
        self.tv = tv
        
    @abstractmethod
    def execute(self):
        pass
    
class TurnOnCommand(Command):
    def execute(self):
        self.tv.turn_on()
        
class TurnOffCommand(Command):
    def execute(self):
        self.tv.turn_off()
        
        
# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None
        
    def set_command(self, command):
        self.command = command
        
    def press_button(self):
        if self.command:
            self.command.execute()
            
# Client code
tv = TV()

turn_on = TurnOnCommand(tv)
turn_off = TurnOffCommand(tv)

remoteControl = RemoteControl()

remoteControl.set_command(turn_on)
remoteControl.press_button()

remoteControl.set_command(turn_off)
remoteControl.press_button()