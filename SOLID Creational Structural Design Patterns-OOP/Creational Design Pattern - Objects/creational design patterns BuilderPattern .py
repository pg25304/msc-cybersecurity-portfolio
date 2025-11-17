class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        return [item.name for item in self.items]

class VegBurger:
    def __init__(self):
        self.name = "Veg Burger"

class ChickenBurger:
    def __init__(self):
        self.name = "Chicken Burger"

class Coke:
    def __init__(self):
        self.name = "Coke"

class Pepsi:
    def __init__(self):
        self.name = "Pepsi"

class MealBuilder:
    def __init__(self):
        self.veg_burger = VegBurger()
        self.chicken_burger = ChickenBurger()
        self.coke = Coke()
        self.pepsi = Pepsi()
    def prepare_veg_meal(self):
        meal = Meal()
        meal.add_item(self.veg_burger)
        meal.add_item(self.coke)
        return meal

    def prepare_non_veg_meal(self):
        meal = Meal()
        meal.add_item(self.chicken_burger)
        meal.add_item(self.pepsi)
        return meal

#client code
builder = MealBuilder()
veg_meal = builder.prepare_veg_meal()
non_veg_meal = builder.prepare_non_veg_meal()
print(veg_meal.show_items())
print(non_veg_meal.show_items())

#client code
#In summary, objects can call methods or access variables from other classes based on inheritance, composition,
# or by having a reference to the target object, as long as the methods and variables are accessible
# (public or protected).
"""In object-oriented programming, an instance or object of a class can indeed call methods or access variables from 
another class in certain scenarios:
Inheritance: When a class inherits from another class, it can access and use the public and protected methods and 
variables of the parent class. In the provided code example, VegBurger, ChickenBurger, Coke, and Pepsi classes do not
inherit from any other class, but if they did, they would be able to call methods and access variables from their
parent class.
Composition: When an object of one class contains a reference to an object of another class, the containing object 
can call methods and access public variables of the contained object. In the given example, the Meal class has a items
attribute, which is a list containing VegBurger, ChickenBurger, Coke, and Pepsi objects. The Meal object can call the
name attribute (public variable) of these objects in the show_items() method.
Inter-object communication: An object can call methods of another object if it has a reference to that object and the
methods are public. In the example, the MealBuilder class creates instances of the Meal, VegBurger, ChickenBurger, 
Coke, and Pepsi classes. The MealBuilder object can call the methods or access variables of these objects
because it has references to them and the methods/variables are public."""