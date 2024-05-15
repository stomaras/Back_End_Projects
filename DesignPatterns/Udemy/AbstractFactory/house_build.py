from abc import ABC, abstractmethod
# Products Furnitures, Electronics and Decorations
class Furniture(ABC):
    def __init__(self, quantity):
        self.quantity = quantity
        
    @abstractmethod
    def display(self):
        pass
    
class Chair(Furniture):
    def display(self):
        return f"{self.quantity} Chair"
    
class Sofa(Furniture):
    def display(self):
        return f"{self.quantity} Sofa"
    
####################PRODUCT 2###################
class Electronic(ABC):
    def __init__(self, quantity):
        self.quantity = quantity
        
    @abstractmethod
    def display(self):
        pass
    
class TV(Electronic):
    def display(self):
        return f"{self.quantity} TV"
    
class Radio(Electronic):
    def display(self):
        return f"{self.quantity} Radio"
    
####################PRODUCT 3###################
class Decoration(ABC):
    def __init__(self, quantity):
        self.quantity = quantity
        
    @abstractmethod
    def display(self):
        pass
    
    
class FlowerVase(Decoration):
    def display(self):
        return f"{self.quantity} Flower Vase"
    
class Chandalier(Decoration):
    def display(self):
        return f"{self.quantity} Chandalier"
    
#################PRODUCT FACTORIES #################

class HouseFactory(ABC):
    @abstractmethod
    def furniture(self):
        pass
    
    @abstractmethod
    def electronic(self):
        pass
    
    @abstractmethod
    def decoration(self):
        pass
    
class SmallHouse(HouseFactory):
    def furniture(self):
        return Chair(4)
    
    def electronic(self):
        return Radio(2)
    
    def decoration(self):
        return FlowerVase(2)
    
class BigHouse(HouseFactory):
    def furniture(self):
        return Sofa(10)
    
    def electronic(self):
        return TV(5)
    
    def decoration(self):
        return Chandalier(5)
    

#client code
def client(factory:HouseFactory):
    print("Furniture:", factory.furniture().display())
    print("Electronic:", factory.electronic().display())
    print("Decoration:", factory.decoration().display())
    print()
    
print("SMALL HOUSE".center(30,'*'))
client(SmallHouse())
    
print("BIG HOUSE".center(30,'*'))
client(BigHouse())
    
    