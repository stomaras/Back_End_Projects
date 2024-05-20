import copy

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def clone(self):
        return copy.deepcopy(self)
    
class EcommercePlatform:
    def __init__(self):
        self.prototype_products = {}
        
    def register_prototype(self, key, prototype_product):
        self.prototype_products[key] = prototype_product
        
    def create_product(self, key, name, price, category):
        prototype_product = self.prototype_products.get(key)
        if prototype_product:
            new_product = prototype_product.clone()
            new_product.name = name
            new_product.price = price
            new_product.category = category
            return new_product
        else:
            return ValueError(f"Prototype with key '{key}' not found")
        
        
ecommerce_platform = EcommercePlatform()

clothing_product = Product("Clothing", 49.99, "Aparel")
electronics_product = Product("Electronics",99.99,"Gadgets")

# Register prototypes
ecommerce_platform.register_prototype("clothing",clothing_product)
ecommerce_platform.register_prototype("electronics",electronics_product)    


product1 = ecommerce_platform.create_product("clothing","T-Shirt",29.99,"Apparel")
product2 = ecommerce_platform.create_product("electronics","T-Shirt",89.00,"Gadhets")

print(product1.name, product1.price, product2.name, product2.price)