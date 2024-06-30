import abc


class OrderProcessingTemplate(metaclass=abc.ABCMeta):
    def process_order(self, order):
        self.validate_payment(order)
        self.update_inventory(order)
        self.generate_shipping_label(order)
        self.send_order_confirmation(order)
        
    @abc.abstractmethod
    def validate_payment(self, order):
        pass
    
    def update_inventory(self, order):
        print(f"Updating inventory for order {order}")
        
    @abc.abstractmethod
    def generate_shipping_label(self, order):
        pass
    
    def send_order_confirmation(self, order):
        print(f"Sending order confirmation for order {order}")
        
class CreditCardOrderProcessing(OrderProcessingTemplate):
    def validate_payment(self, order):
        print(f"Validating payment for order {order} using credit card")
        
    def generate_shipping_label(self, order):
        print(f"Generating shipping label for order {order} using credit card")
        
class PayPalOrderProcessing(OrderProcessingTemplate):
    def validate_payment(self, order):
        print(f"Validating payment for order {order} using PayPal")
    
    def generate_shipping_label(self, order):
        print(f"Generating shipping label for order {order} using PayPal")
        
    
if __name__ == "__main__":
    credit_card_order = CreditCardOrderProcessing()
    credit_card_order.process_order("12345")
    
    paypal_order = PayPalOrderProcessing()
    paypal_order.process_order("67890")
    