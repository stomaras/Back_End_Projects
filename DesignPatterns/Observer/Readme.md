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