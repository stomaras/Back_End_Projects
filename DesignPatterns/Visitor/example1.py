# element

# these behaviours are called visitors. They visit the element and they perfrom operations with the element without 
# being coupled into the  element themselves.
# behavior1, behavior2 - visitor

from abc import ABC, abstractmethod

class Visitor(ABC):
    
    # visit method is what interact with the element.
    @abstractmethod
    def visit(self, element):
        pass


# Concrete Visitor1
class ConcreteVisitor1(Visitor):
    def visit(self, element):
        element.operation1()
        
# Concrete Visitor2
class ConcreteVisitor2(Visitor):
    def visit(self, element):
        element.operation2()
        
        
# Element interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass
    
class ConcreteElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit(self)
        
    def operation1(self):
        print("ConcreteElementA operation1")
        
    def operation2(self):
        print("ConcreteElementA operation2")
        
        
# Client code:
if __name__ == '__main__':
    
    element_a = ConcreteElementA()
    
    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()
    
    element_a.accept(visitor1)
    element_a.accept(visitor2)
    
    
    