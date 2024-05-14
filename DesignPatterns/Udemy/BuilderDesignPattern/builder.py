# Real World cases
# Document Creation: pdf or html files 
# GUI Creation: complex user interfaces with different layers, options
# Meal Ordering : create different meal orders such as toppings, sides and beverages
# Car manufacturing: create cars with different options and configurations such as engine, size , color and features

# Terminologies

# Product: the complex object being constructed. It has multiple parts and requires a step-by-step process to construct. This could
# be any object like database query, game, nextwork, website object etc

# Builder : an abstract interface that defines the steps required to build an object. It declares methods for creating and 
# assembling parts of the product.

# Concrete Builder: a concrete implementation of the Builder Interface that provides an implementation for each of Builder
# methods. It defines and keeps track of the representation it creates.

# Director: a class that controls the construction process. It knows which builder to use and in what order 
# to call the Builder methods to create a product.

# Client: a class or module that uses the builder pattern to create the product. It is responsible for creating the Director
# object and configuring it with the appropriate Builder. The client can also work directly with the builder if it needs 
# more control over the construction process.