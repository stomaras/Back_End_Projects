# Document Processing
# Logging Frameworks : Logging Frameworks utilize the Factory Method pattern to create different loggers based on the desired o/t
# such as console loggers , file loggers and db loggers
# Database Connectivity : Database Connectivity libraries may employ the Factory Method pattern to create specific database connection
# objects for different database vendors, like MySQL, PostgreSQL, Oracle
# Payment Gateway : Payment Gateway integrations can use the Factory Method pattern to create instances of different payment gateway classes
# based on the selected Provider: such as Paypal, Stripe or Braintree

# Terminologies

# Product: It refers to the abstract base class or interface that defines the common methods and properties that all products(objects)
# created by the factory will have

# Concrete Product: These are the concrete products. Each concrete product represents a specific variation or type of object that can be 
# created by the factory

# Creator: The creator is the abstract base class or interface that declares the factory method. It provides the contract for creating
# objects bu does not specify the concrete class

# Concrete Creator: These are the concrete creators. Each concrete creator is responsible for creating a specific type of product.

# Factory Method: The factory method is a method that is defined in the creator class. It is responsible for creating the concrete product

#Client: The client is the code that uses the factory method to create objects. It interacts with the creator through the abstract class
# or interface, without being aware of the concrete classes being instantiated