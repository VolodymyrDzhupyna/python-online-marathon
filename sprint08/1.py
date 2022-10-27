import unittest


def get_discount(count_discount):

        if count_discount > 20:
            return .5
        elif count_discount >= 20:
            return .7
        elif count_discount >= 10:
            return .8
        elif count_discount >= 7:
            return .9
        elif count_discount >= 5:
            return .95
        else:
            return 1

class Product:
    
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    
    def __init__(self, *products_list):
        self.products_list = products_list
    
    def get_total_price(self):
        total_price = sum([item.price * item.count * get_discount(item.count) for item in self.products_list[0]])
        return total_price

        
class CartTest(unittest.TestCase):
    
    products = (Product('p1',10,4),
            Product('p2',100,5),
            Product('p3',200,6),
            Product('p4',300,7),
            Product('p5',400,9),
            Product('p6',500,10),
            Product('p7',1000,20))
    cart = Cart(products)

    def test_get_total_price(self):
        self.assertEqual(self.cart.get_total_price(), 24785.0)
        

products = (Product('p1',10,4),
Product('p2',100,5),
Product('p3',200,6),
Product('p4',300,7),
Product('p5',400,9),
Product('p6',500,10),
Product('p7',1000,20))
cart = Cart(products)
print(cart.get_total_price())
