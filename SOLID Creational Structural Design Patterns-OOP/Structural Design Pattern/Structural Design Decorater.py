#coffee shop example using decorator pattern
#Base class representing a simple coffee
#cost() returns 5 (base price of coffee)
class Coffee:
    def cost(self):
        return 5
#Abstract decorator class that wraps a coffee object
#__init__(): Stores a reference to a coffee object via self._coffee
#cost(): Returns the cost of the wrapped coffee (delegates to it)
#This is the base decorator — child decorators will override cost()
class CoffeeDecorator:
    def __init__(self, coffee ):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost()
#Inherits from CoffeeDecorator
#cost(): Adds 1 to the wrapped coffee's cost (milk adds $1)
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5
#Creates a simple coffee ($5)
#Wraps it with MilkDecorator (<span>5 +</span>1 = $6)
#Wraps the milk coffee with SugarDecorator (<span>6 +</span>0.50 = $6.50)
#Prints the cost at each step
if __name__ == "__main__":
    simple_coffee = Coffee()
    print(f"simple coffee is: ${simple_coffee.cost()}")

    milk_coffee =MilkDecorator(simple_coffee)
    print(f"coffee with milk is: ${milk_coffee.cost()}")

    sugar_coffee =SugarDecorator(milk_coffee)
    print(f"milk coffee plus sugar is:${sugar_coffee.cost()}")

#if __name__ == "__main__": is a Python idiom that checks if the script is being run directly (not imported as a module).
#ow it works:
#When you run a script directly: python script.py, Python sets __name__ to "__main__"
#When you import a script as a module: import script, Python sets __name__ to the module name (e.g., "script")