##### Template Method Components #######
#1. abstract class - defines the overall algorithm / structure
#2. Template methods - series of method calls that represents the steps of the algorithm
    #b. abstract class - must be declare
    #b. Hook methods - optional methods or default implementation for all subclasses.
    
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.initialize()
        self.perform_algorithm()
        self.cleanup()
        
    def initialize(self):
        print("Initializing the algorithm...")
    
    @abstractmethod
    def perform_algorithm(self):
        pass
    
    def cleanup(self):
        print("Cleaning up the algorithm...")
        
class ConcreteClass1(AbstractClass):
    def perform_algorithm(self):
        print("ConcreteClass1 performing algorithm...")

class ConcreteClass2(AbstractClass):
    def perform_algorithm(self):
        print("ConcreteClass2 performing algorithm...")
        
concrete_object1 = ConcreteClass1()
concrete_object1.template_method()

concrete_object2 = ConcreteClass2()
concrete_object2.template_method()