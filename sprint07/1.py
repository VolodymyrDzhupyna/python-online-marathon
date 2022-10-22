from abc import abstractmethod


class Product:
    
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    name = "Fettuccine Alfredo"
    
    def cook(self):
        print(f"Italian main course prepared: {self.name}")


class Tiramisu(Product):
    name = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name}")


class DuckALOrange(Product):
    name = "Duck À L'Orange"
    
    def cook(self):
        print(f"French main course prepared: {self.name}")


class CremeBrulee(Product):
    name = "Crème brûlée"
    
    def cook(self):
        print(f"French dessert prepared: {self.name}")


class Factory:
    
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        if type_of_meal == "dessert":
            return Tiramisu()


class FrenchDishesFactory(Factory):

    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        if type_of_meal == "dessert":
            return CremeBrulee()


class FactoryProducer:

    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory()
        if type_of_factory == "french":
            return FrenchDishesFactory()


p = Product()
fetalf = FettuccineAlfredo()
fetalf.cook()
tir = Tiramisu()
tir.cook()
duckal = DuckALOrange()
duckal.cook()
cremebr = CremeBrulee()
cremebr.cook()
f = Factory()
italf = ItalianDishesFactory()
print(italf.get_dish("main"))
print(italf.get_dish("dessert"))
fref = FrenchDishesFactory()
print(fref.get_dish("main"))
print(fref.get_dish("dessert"))
fprod = FactoryProducer()
print(fprod.get_factory("italian"))
print(fprod.get_factory("french"))
