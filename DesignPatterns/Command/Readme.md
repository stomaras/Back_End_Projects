# Terminologies

- command: An interface or abstract class that declares the excution method execute(). It represents a request and provides a common 
interface for all concrete command objects.

- concreteCommand: The implementation classes that encapsulate specific requests and bind them to receivers. They implement the excute() method by invoking the corresponding operations on the receiver.

- Receiver: The class that contains the actual business logic or operations that fulfill the requests received from commands. It defines the actions that the ConcreteCommand objects can perform.

- Invoker: The class that holds a reference to a command object that is responsible for executing the command when requested.It invokes the execute() method on the command, but it does not know the specific command implementation.