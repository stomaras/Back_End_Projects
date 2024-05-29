"""
Subsystems
    - Product
    - Inventory
    - Payment
Facade
    - Online Store    
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
class Inventory:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def remove_product(self, product):
        self.products.remove(product)
        
    def get_products(self):
        return self.products
    
class Payment:
    def __init__(self):
        self.total = 0
        
    def add_product(self, product):
        self.total += product.get_price()
        
    def remove_product(self, product):
        self.total -= product.get_price()
        
    def get_total(self):
        return self.total
    
#Facade
class OnlineStore:
    
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
    
    def add_product_to_cart(self, name, price):
        product = Product(name, price)
        self.inventory.add_product(product)
        self.payment.add_product(product)
    
    def remove_product_from_cart(self, name):
        products = self.inventory.get_products()
        
        for product in products:
            if product.get_name() == name:
                self.inventory.remove_product(product)
                self.payment.remove_product(product)
                break
            
    def checkout(self):
        total = self.payment.get_total()
        print(f"Total: {total}")
        
    def cart_list(self):
        products = self.inventory.get_products()
        for product in products:
            print(f"{product.get_name()}: {product.get_price()}")
        
        
if __name__ == "__main__":
    online_store = OnlineStore()
    online_store.add_product_to_cart("iPhone", 1000)
    online_store.add_product_to_cart("MacBook", 2000)
    online_store.checkout()
    online_store.remove_product_from_cart("iPhone")
    online_store.checkout()
    online_store.cart_list()