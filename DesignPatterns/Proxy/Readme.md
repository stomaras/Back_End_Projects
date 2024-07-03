- The Proxy Design Pattern is a behavioural pattern that allows a client to interact with an object indirectly through a proxy object.
The proxy object act as an intermediary between the client and the real object, providing additional functionality, such as caching, security, or remote access.

- In the Proxy Design Pattern, the proxy object has the same interface as the real object, so the client can use it interchnageably with the real object. The client is unaware that is using a proxy object, as the proxy object transparently forwards requests to the real object, and may also perfrom additional tasks before or after forwarding the request.

- The proxy design pattern can be used in situations where the real object is resource-intensive to create, or where access to real object needs to be controlled or secured. It can also be used to add additional functionality to an object, such as logging, without modifying the original object's code.

# Terminologies

- Subject: This is the common interface or abstract class that both the RealSubject and Proxy classes implement. It defines the common operations that both classes can perform.

- RealSubject: This is the real object that the Proxy represents. It implements the operations defined in the Subject interface.

- Proxy: This is an object that acts as an intermediary between the client and the RealSubject. It implements the same interface as the RealSubject and forwards requests from the client to the RealSubject, addding its own behavior before or after forwarding the request.

- Client: This is the object that interacts with the Proxy object to perfrom operations on the RealSubject. The client interacts with the Proxy object in the same way as it would with the RealSubject object, without being aware of the actual object it is working with.