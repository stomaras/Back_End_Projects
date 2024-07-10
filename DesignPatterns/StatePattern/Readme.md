# Context:
The context refers to the object that contains the state and whose behavior is affected by the state. It maintains a reference to the 
current state object and delegates the state-specific behavior to that object. The context class defines methods and properties that are used by the state objects to transition between states.

# State:
The state represents a specific behavior or a state of the context object. It is usually implemented as an interface or an abstract class that defines a set of methods that the context can call to perform state-specific operations. Each state class provides its own implementation for these methods.

# Concrete State:
are the specific implementations of the state interface or abstract class. Each concrete state class represents a particular state of the context object and provides the implementation for the methods defined in the state interface.

# Transition:
A Transition occurs when the context object changes its state from one state to another. It is usually triggered by a specific event 
or condition that causes the context to transition to a different state. Transitions are handled by the state object themselves, as they decide which state to transition to based on the current state and the trigerring event.