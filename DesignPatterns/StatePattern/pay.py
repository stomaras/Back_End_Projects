from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number, expiry_data, cvv):
        self.card_number = card_number
        self.expiry_data = expiry_data
        self.cvv = cvv
        
    def pay(self, amount):
        print(f"Credit Card Payment: {amount} using card {self.card_number}")
        
class PayPalStrategy(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def pay(self, amount):
        print(f"PayPal Payment: {amount} using email {self.email}")
        
        
# step 3: Create the Context class
class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
        
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
        
    def process_payment(self, amount):
        self.payment_strategy.pay(amount)
        
        
# Step 4: Clinet code
amount = 100

processor = PaymentProcessor(CreditCardStrategy("123456789","12/25","123"))

processor.process_payment(amount)
processor.set_payment_strategy(PayPalStrategy("sptom@gmail.com", "password"))
processor.process_payment(amount)