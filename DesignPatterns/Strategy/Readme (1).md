# Strategy Design Pattern

- is a behavioural design pattern that allows you to define a family of algorithms, encapsulate each one as a separate class, and make them interchaengeable.
  It enables the algorithms to vary independently from the clients that use them, allowing runtime selection of the algorithm based on the specific requirements.

- The main idea behind the Strategy pattern is to encapsulate a group of related algorithms and provide a common interface for them. This interface defines a set of methods or operations that the algorithm must implement. The client code can then utilize these algorithms by interacting with the common interface without knowing the specific implementation details of each algorithm.

# Real world cases of strategy design pattern.

- Sorting Algorithms: Different sorting algorithms, such as bubble sort, merge sort, or quicksort, can be encapsulated as strategies. The sorting algorithm can be selected at runtime based on the size of the data or other factors.
- Payment Processing: In payment systems, different payment methods (e.g, credit card, Paypal, bank transfer) can be implemented as strategies. The payment method can be selected by the user or based on certain conditions.
- File Compression Utility: Various compression algorithms, such as ZIP, GZIP or RAR, can be implemented as strategies. The compression algorithm can be selected based on the type of file or desired compression level.
  e.t.c

# Terminologies

- Context: The Context is the class or object that contains the business logic or behavior that needs to be performed. It maintains a reference to a Strategy object and uses it to execute
  the desired algorithm. The Context is responsible to invoking the algorithm through the strategy interface without knowing the specific implementation details of the chosen strategy.

- Strategy: The Strategy is an interface or abstract class that defines the common methods or operations that the different algorithms must implement. It encapsulates the algorithmic bahavior and provides a standardized way for the Context to interact with the algorithms. The Strategy declares the methods that the Context will use to delegate the execution of the algorithm.

- Concrete Strategies: The Concrete Strategies are the actual implementations of the Strategy interface. Each concrete strategy encapsulates a specific algorithm or behavior. These classes
  provide the detailed implementation of the algorithm defined by the Strategy interface. Multiple Concrete Strategy classes can be created to represent different variations or versions of the algorithm.

