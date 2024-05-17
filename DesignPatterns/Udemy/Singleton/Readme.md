# The Singleton design pattern is a design pattern that ensures a class has only one instance and provides 
# a global point of access to it

# It is often used for objects that need to be shared across the entire application, such as logging, database connections, and
# configuring settings.

# The basic implementation of the Singleton Pattern involves creating a private constructor, a static instance variable, and a static 
# method returns the instance.

# The instance is created the first time the method is called, and all subsequent calls return the same instance

# Terminologies Singleton Pattern

# 1. Singleton: The Singleton class itself, which ensures that only one instance of the class can be created and provides a global 
# point of access to that instance.

# 2. Instance: The Single object created by the Singleton class. It is the sole instance of the class that is shared and accessed by different parts of the code.

# 3. getInstance(): A static method of the Singleton class that provides access to the single instance. It creates the instance if it 
# does not exist, or returns the existing instance if it has already been created.

# 4. __instance: A private static variable within the Singleton class that holds the single instance. It is typically a class-level
# variable that is shared by all instances of the class.

# 5. init(): A private constructor method of the Singleton class. It ensures that the class cannot be directly instantiated by external code. Instead, the getInstance() method should be used to obtain the instance.