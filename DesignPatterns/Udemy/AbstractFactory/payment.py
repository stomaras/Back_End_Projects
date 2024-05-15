from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount:float)->str:
        pass
    
class CreditCard(PaymentMethod):
    def make_payment(self, amount:float)->str:
        print(f"Pay {amount} using Credit Card")
        
class DebitCard(PaymentMethod):
    def make_payment(self, amount:float)->str:
        print(f"Pay {amount} using Debit Card")
        
class Remita(PaymentMethod):
    def make_payment(self, amount:float)->str:
        print(f"Pay {amount} using Remita")
        
class NetBanking(PaymentMethod):
    def make_payment(self, amount:float)->str:
        print(f"Pay {amount} using NetBanking")
        
# =====================Payment Factory =================

class PaymentFactory(ABC):
    def create_payment(self, payment_method):
        if payment_method in self.payments:
            return self.payments.get(payment_method)()
    
class USPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card= CreditCard, debit_card=DebitCard, netbanking=NetBanking)
        
class CanadaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard, netbanking=NetBanking)


class Client:
    def __init__(self):
        self.factory = None
        
    def get_factory(self):
        country_factory = dict(us=USPaymentFactory, canada=CanadaPaymentFactory)
        
        flist = " ,".join(country_factory)
        while not self.factory:
            country = input(f"Enter Country Payment({flist}):")
            
            if country in country_factory:
                self.factory = country_factory.get(country)()
                break
            print(f"You need to enter one of the countries listed ({flist})")
            
    def do_payment(self):
        if self.factory:
            amount = float(input("How much are you paying:"))
            available_payments = ", ".join(self.factory.payments)
            payment_method = input(f"Enter Your Payment Method:({available_payments}):")
            if payment_method in self.factory.payments:
                payment = self.factory.payments.get(payment_method)()
                payment.make_payment(amount)
            else:
                print(f"You need to enter one of the payment methods listed ({available_payments})")
        else:
            print("You need to select a country first")
            
    def run_payments(self):
        self.get_factory()
        self.do_payment()
        
if __name__ == "__main__":
    client = Client()
    client.run_payments()          
    