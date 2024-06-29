from abc import ABC, abstractmethod

class Event: #Event Object
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data
        
# The event handler class manages the observer and handles the notifications process.
class EventHandler:
    def __init__(self):
        self.observers = {}
        
    def attach(self, event_type, observer):
        if event_type not in self.observers:
            self.observers[event_type] = []
        self.observers[event_type].append(observer)
        
    def detach(self, event_type, observer):
        if event_type in self.observers:
            self.observers[event_type].remove(observer)
            
    def notify(self, event):
        event_type = event.event_type
        if event_type in self.observers:
            for observer in self.observers[event_type]:
                observer.update(event)
                
class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass
    
class ButtonClickObserver(Observer):
    def update(self, event):
        if event.event_type == "button_click":
            print("Button Clicked:", event.data)
            
class MouseMoveObserver(Observer):
    def update(self, event):
        if event.event_type == "mouse_move":
            print("Mouse Moved:", event.data)
            
            
# client
event_handler = EventHandler()

button_observer = ButtonClickObserver()
mouse_observer = MouseMoveObserver()


event_handler.attach("button_click", button_observer)
event_handler.attach("mouse_click", mouse_observer)

event_handler.notify(Event("button_click", "Left"))
event_handler.notify(Event("mouse_move", "(100,200)"))