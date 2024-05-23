# Component : This is the common interface shared by all objects in the composition.It declares the methods that are common 
# to both simple and complex objects.

# Leaf: This is the basic implementation of the Component interface. A Leaf object does not have any children.

# Composite: This is a complex implementation of the Component interface. It can contain other Components, including other 
# Composite objects.

# Client: This is the code that uses the Component interface to interact with the objects in the composition.

# Recursive Composition: This is the key feature of the Composite pattern, where a Composite object can contain other Composite objects 
# in a recursive manner, forming a tree-like structure. This allows clients to treat all objects in the tree uniformly, whether they are
# simple Leaf objects or complex Composite objects