class Goods: 
  
    def __init__(self, price, discount_strategy = None): 
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount
    
    def __str__(self):
        result = f"Price: {self.price}, price after discount: {self.price_after_discount()}"
        return result

def on_sale_discount(order): 
    return order.price * 0.5

def twenty_percent_discount(order):
    return order.price * 0.2


print(Goods(20000))
print(Goods(20000, discount_strategy = twenty_percent_discount))
print(Goods(20000, discount_strategy = on_sale_discount))
 