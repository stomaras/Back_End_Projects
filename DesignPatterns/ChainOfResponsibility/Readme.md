- The Chain of Responsibility is a behavioural design pattern that provides a way to pass a request along a chain of potential
handlers until one of them handles the request. The pattern decouples senders and receivers of a request, allowing multiple objects
to have a chance to handle the request without explicitly knowing which object will handle it.

- When a client sends a request, it is received by the first handler in the chain. This handler examines the request and decides whether
it can handle it or not. If it can, it processes the request and completes the handling.If not, it passes the request to the next handler in the chain.

# Real World Case:

- Middleware in Web Development: Web frameworks often use the Chain of Responsibility pattern to implement middleware functionality.
Middleware components in the chain process incoming HTTP requests and can perform various tasks such as authentication, request parsing, request validation, or logging. Each middleware component can decide to handle the request or pass it to the next middleware in the chain.

# Terminologies

- Handler: Also known as the Abstract Handler or Base Handler, it is an interface or abstract class that defines the common interface
for all concrete handlers. It declares the handle_request() method that concrete handlers must implement. The handler usually contains a reference to the next handler in the chain.

- Concrete handler: it is a concrete implementation of the Handler interface or abstract class. Each concrete handler decides whether it can handle a request or not. If it can handle the request, it processes it, otherwise, it passes the request to the next handler in 
the chain.

- Successor: It refers to the next handler in the chain. Each handler has a reference to its successor, which allows the request to be passed along the chain until it is handled or until the end of the chain is reached. The successor can be set or modified dynamically.

- Client: The client initiates the request and starts the processing chain. It is responsible for creating the chain of handlers and sending the request to the first handler in the chain.

- Request: It represents the request being passed through the chain of handlers. The request can be a specific object or data structure
that encapsulates the information or context required for handling and processing.