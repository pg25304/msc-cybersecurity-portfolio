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
    def prepare_veg_meal(self):
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal

    def prepare_non_veg_meal(self):
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal

#client code
builder = MealBuilder()
veg_meal = builder.prepare_veg_meal()
non_veg_meal = builder.prepare_non_veg_meal()
print(veg_meal.show_items())
print(non_veg_meal.show_items())

#client code
