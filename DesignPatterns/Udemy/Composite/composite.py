'''
COMPOSITE
    - component
    - component
    - COMPOSITE
        - component
        - component
        - COMPOSITE
            - component
'''

class Component:
    def __init__(self, name):
        self.name = name
        
    def operation(self):
        print(f'{self.name}: Performing operation')
        

class Composite:
    def __init__(self, name):
        self.name = name
        self.children = []
        
    def add(self, component):
        self.children.append(component)
        
    def remove(self, component):
        self.children.remove(component)
        
    def operation(self):
        print(f'{self.name}: Performing operation')
        for child in self.children:
            child.operation()
            
leaf1 = Component('leaf 1')
leaf2 = Component('leaf 2')

composite = Composite('composite 1')
composite.add(leaf1)
composite.add(leaf2)

composite.operation()
        