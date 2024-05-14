from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car started")
        
class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started")
        
class Bicycle(Vehicle):
    def start(self):
        print("Bicycle started")
        
class VehicleFactory():
    def __init__(self):
        self.factory = dict(car= Car, motorcycle= Motorcycle, bicycle = Bicycle)
        
    def create_vehicle(self, vehicle_type):
        if vehicle_type in self.factory:
            vehicle = self.factory.get(vehicle_type)
            return vehicle()
        
if __name__ == '__main__':
    factory = VehicleFactory()
    car = factory.create_vehicle("bicycle")
    car.start()