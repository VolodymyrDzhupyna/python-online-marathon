class Pizza:
    order_count = 0

    def __init__(self, ingredients):
        self._ingredients = ingredients
        Pizza.order_count += 1
        self._order_number = Pizza.order_count
	
    @property
    def order_number(self):
        return self._order_number

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self._ingredients = ingredients

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])
		
    @classmethod    
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod	
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])


p1 = Pizza(['bacon', 'parmesan', 'ham'])
print(p1.ingredients)
	
p2 = Pizza.garden_feast()
print(p2.ingredients)

p3 = Pizza.hawaiian()
print(p3.ingredients)

p4 = Pizza.meat_festival()
print(p4.ingredients)

p5 = Pizza(["pepperoni", "bacon"])
print(p5.ingredients)

print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
