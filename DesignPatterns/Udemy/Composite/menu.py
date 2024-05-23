'''
Menu
    - MenuItem
    - MenuItem
    - Menu
        - MenuItem
        - MenuItem
'''

# leaf item, component
class MenuItem:
    def __init__(self, name):
        self.name = name
        
    def ls(self):
        print(self.name)
        
# composite
class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
    
    def ls(self):
        print(self.name)
        for item in self.items:
            item.ls()
            
item = MenuItem('item1')
item2 = MenuItem('item2')

menu = Menu('menu1')
menu.add_item(item)
menu.add_item(item2)

menu.ls()