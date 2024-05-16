from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def display(self):
        pass
    
#==================CHARACTERS =============================
class Character(GameObject):
    def display(self):
        pass
    
class Knight(Character):
    def display(self):
        print("Knight Character")

class Astranault(Character):
    def display(self):
        print("Astranault Character")

class Soldier(Character):
    def display(self):
        print("Soldier Character")
    
#==================WEAPONS =============================
class Weapon(GameObject):
    def display(self):
        pass
    
class MachineGun(Weapon):
    def display(self):
        print("MachineGun Weapon")
        
class LightSaber(Weapon):
    def display(self):
        print("LightSaber Weapon")
        
class Sword(Weapon):
    def display(self):
        print("Sword Weapon")
        
#===================LEVELS =============================

class Level(GameObject):
    def display(self):
        pass
    
class Garage(Level):
    def display(self):
        print("Garage Level")
        
class SpaceShip(Level):
    def display(self):
        print("SpaceShip Level")

class Castle(Level):
    def display(self):
        print("Castle Level")
        
#==================Abstract Factory======================

class GameFactory(ABC):
    @abstractmethod
    def create_character(self):
        pass
    
    @abstractmethod
    def create_weapon(self):
        pass
    
    @abstractmethod
    def create_level(self):
        pass
    
class ModernGameFactory(GameFactory):
    def create_character(self): 
        return Soldier()
    
    def create_weapon(self):
        return MachineGun()
    
    def create_level(self):
        return Garage()
    
class MedievalGameFactory(GameFactory):
    def create_character(self):
        return Knight()
    
    def create_weapon(self):
        return Sword()
    
    def create_level(self):
        return Castle()
    
class ScifiGameFactory(GameFactory):
    def create_character(self):
        return Astranault()
    
    def create_weapon(self):
        return LightSaber()
    
    def create_level(self):
        return SpaceShip()
    
def client():
    factories = dict(medieval = MedievalGameFactory, scifi = ScifiGameFactory, modern = ModernGameFactory)
    
    factory_list = ", ".join(factories) # medieval, scifi, modern
    while True:
        factory_type = input(f"Enter the type of Game ({factory_list}) :")
        
        if factory_type in factories:
            break
        print(f"Try Again. This game type does not exist. Choose between {factory_list}")
        
    return factories.get(factory_type)()

if __name__ == "__main__":
    factory = client()
    
    # Create character
    character = factory.create_character()
    character.display()
    
    # Create Weapon
    weapon = factory.create_weapon()
    weapon.display()
    
    # Create Level
    level = factory.create_level()
    level.display()
    