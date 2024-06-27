- The Observer design pattern is a behavioural design pattern that establishes a one-to-many dependency between objects.
It defines a subscription mechanism, where one object (called the subject or observable) maintains a list of other objects (called observers) and notifies them automatically of any changes in its state.

- The main goal of the Observer pattern is to ensure that multiple observers can be notified and updated when the state of the subject
changes, without the subject needing to have direct knowledge of the observers. This promotes loose coupling between the subject and the observers, enabling a more flexible and maintainable system.

- In the Observer pattern, the subject maintains a list of observers and provides methods to subscribe and unsubscribe observers.
When the subject's state changes, it notifies all the subscribed observers, typically by invoking a method on each observer.
The observers can then perform their specific logic based on the updated information received from the subject.

Use cases:

- Stock Market: In a stock market, various investors or traders subscribe to receive updates on the price changes or specific stocks.
The stock market act as the subject, and the invenstors are the observers. Whenever the price of a stock changes, the stock market notifies all the subscribed investors, allowing them to make informed decisions.

- Social Media Notifications: Users can subscribe to receive notifications about new messages, friend requests, comments, or likes.
The social media platform acts as the subject, and the users are observers. When a new information is generated, the platform notifies the subscribed users, ensuring they are promptly informed about relevant activities.

# Terminologies

- Subject (also known as Observable or Publisher): It is the object that maintains a list of observers and sends notifications to them 
when its state changes. The subject provides methods to subscribe, unsubscribe, and notify observers.

- Observer (also knows as Subscriber or Listener): It is the interface or base class implemented by the observers. The observer defines
the update method that is called by the subject when a state change occurs. Observers are the recipients of notifications from the subject.

- ConcreteSubject (also known as ConcreteObservable or ConcretePublisher): It is a specific implementation of the subject interface or class. The concrete subject holds the actual state and sends notifications to the registered observers when changes occur.

- ConcreteObserver (also known as ConcreteSubscriber or ConcreteListener): It is a specific implementation of the observer interface or class. The concrete observer defines the logic to be executed when an update is received from the subject. Multiple concrete observers can exist, each implementing the update method.

- Subscription: It refers to the process of an observer registering with a subject to receive notifications. When an observer subscribes, it is added to the subject's list of observers.

- Unsubscription: It refers to the process of an observer unregistering from the subject. When an observer unsubscribes, it is removed from the subject's list of observers and will no longer receive notifications.

- Notification: It is the act of informing the observers about a state change in the subject. When a subject's state changes, it iterates over its list of observers and calls their respective update methods to notify them about the change.

- State: It represents the data or condition being observed by the subject. When the state of the subject changes, it triggers noifications to the registered observers.