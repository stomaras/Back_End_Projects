# state
from abc import ABC, abstractmethod

class TrafficLightState(ABC):
    @abstractmethod
    def display_light(self):
        pass
    
    @abstractmethod
    def change_state(self, traffic_light):
        pass


class RedState(TrafficLightState):
    def display_light(self):
        return "Red"
    
    def change_state(self, traffic_light):
        print("Changing from red to green")
        traffic_light.state = GreenState()
        
class GreenState(TrafficLightState):
    def display_light(self):
        return "Green"
    
    def change_state(self, traffic_light):
        print("Changing from green to yellow")
        traffic_light.state = YellowState()
        
class YellowState(TrafficLightState):
    def display_light(self):
        return "Yellow"
    
    def change_state(self, traffic_light):
        print("Changing from yellow to red")
        traffic_light.state = RedState()



# context
class TrafficLight:
    def __init__(self):
        self.state = RedState()
        
    def display_light(self):
        return self.state.display_light()
    
    def change_state(self):
        self.state.change_state(self)
        
        
# usage example
traffic_light = TrafficLight()

print(traffic_light.display_light())
traffic_light.change_state()
print(traffic_light.display_light())
traffic_light.change_state()
print(traffic_light.display_light())
