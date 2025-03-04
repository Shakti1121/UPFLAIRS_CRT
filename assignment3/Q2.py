# 2. Class Product with discount calculation
class Product:
    discount_rate = 0.1  # Class variable
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discounted_price(self):
        return self.price * (1 - Product.discount_rate)

product = Product("Laptop", 1000)
print(product.discounted_price()) 


