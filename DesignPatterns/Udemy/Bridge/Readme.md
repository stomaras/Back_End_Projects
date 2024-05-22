The Bridge Pattern is a design pattern used in object-oriented software development that aims to decouple
an abstraction from its implementation, allowing both to vary independently. It involves creating two separate 
hierarchies of classes, one for the abstraction and one for the implementation,
and then connecting them through a bridge object.

The Bridge Pattern typically involves creating an abstraction class or interface 
that defines the methods and properties that clients will use, and then implementing that abstraction in concrete subclasses
or classes that provide the specific behavior. The abstraction class will then use an instance of the implementation class
through a bridge object to perform the desired behavior.

A Colored Shape
    - Shape is the Abstraction - the main object to create 
        - Circle(Shape), Square(Shape)
    - Color is the implementation - Attribute to define the object
        - Red(Color), Blue(Color)
    - Line is also an implementation
        - A thick(Line), Thin(Line)

Create The Abstraction with an implementation e.g Circle(Red)
    - Use an abstraction method to bridge e.g. get_color() method to paint the Color of the Circle

Terminologies:

# 1. Abstraction: it defines the high-level interface of the system and provides a way to access the implementation
# details through a bridge object

# 2. Refined Abstraction: It extends the Abstraction and adds more specific functionality by working with the implementation
# objects through the bridge.

# 3. Implementation: It defines the interface for the implementation objects and provides a way for the abstraction to access them

# 4. Concrete implementation: It implements the interface defined by the implementation and provides the actual implementation for
# the functionality.

# 5.Bridge: It decouples the abstraction and implementation by providing a way for the abstraction to work with the implementation
# objects through the bridge object.