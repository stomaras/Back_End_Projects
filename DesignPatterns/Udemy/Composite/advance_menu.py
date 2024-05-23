from abc import ABC, abstractmethod

class MenuComponent(ABC):
    def __init__(self,name):
        self.name = name
        
    @abstractmethod
    def display(self):
        pass
    
class MenuComposite(MenuComponent):
    
    @abstractmethod
    def add(self, menu_component):
        pass
    
    @abstractmethod
    def remove(self, menu_component):
        pass
    
class MenuItem(MenuComponent):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price
        
    def display(self):
        print(f'{self.name} - ${self.price}')
        
class Menu(MenuComposite):
    def __init__(self, name):
        super().__init__(name)
        self.menu_components = []
        self.items = []
        
    def add(self, item):
        self.items.append(item)
        
    def remove(self, item):
        self.items.remove(item)
        
    def display(self):
        print(f'Menu: {self.name}')
        for item in self.items:
            item.display()
            
            
main_menu = Menu("Main Menu")

breakfast = Menu("Breakfast Menu")
lunch = Menu("Lunch Menu")
dinner = Menu("Dinner Menu")


breakfast.add(MenuItem("Bread", 8))
breakfast.add(MenuItem("Pancake",8))


main_menu.add(breakfast)

main_menu.display()