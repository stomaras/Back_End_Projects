# The Object Pool design pattern is a creational design pattern tha manages a pool or a cache of reusable objects
# It aims to improve performance and resource utilization by reusing objects instead of creating new ones.This pattern is particularly
# useful when the const of object creation, initialization, or destruction is high.

# In the Object Pool Pattern, a pool of objects is created and managed by a pool manager.
# When an object is needed, instead of creating a new object from scratch, the pool manager 
# provides an existing object from the pool. When the object is no longer needed, it is returned 
# to the pool for future reuse.This way, the overhead of object creation and destruction is reduced

# Object Pool real use cases:

# 1. Object Pooling in Object Relational Mapping(ORM): ORM frameworks often use an Object Pool to manage database entity objects, 
# improving performance by reusing existing objects instead of creating new ones for each database query.

# Terminologies

# 1. Object Pool: The central component of the pattern that manages the pool of reusable objects.
# 2. Object: The objects that are created and managed by the pool. These objects are typically expensive to create or initialize.
# 3. Pool Manager: The entity responsible for managing the Object Pool. It handles the creation, allocation and deallocation of objects # in the pool.
# 4. Available Objects: The collection of objects in the pool that are currently not in use and available fo allocation.
# 5. In-Use Objects: The collection of objects that have been allocated and are currently being used by clients.
# 6. Object creation: The process of instantiating new objects in the pool. This step typically occurs during the initialization of the pool.
# 7. Object allocation: The process of providing an available object from the pool to a client who requests it.
# 8. Object deallocation: The process of returning an object from the pool when it is no longer needed by the client.
# This step may involve resetting or reinitializing the object.
# 9. Pool Size: The maximum number of objects that the pool can hold. It determines the capacity and scalability of the pool.
# 10. Client: The entity that requests objects from the Object Pool for temporary use.
# 11. Object Reset/Reinitialization: The process of restoring an object to its initial state when it is returned to the pool.
# This step ensures that the object is clean and ready for reuse.