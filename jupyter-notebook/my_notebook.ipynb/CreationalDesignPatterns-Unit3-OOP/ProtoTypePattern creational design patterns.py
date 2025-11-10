"""Imports the standard library copy module.
copy provides copy.copy() (shallow copy) and copy.deepcopy() (deep copy).
Concept: this is the Prototype design pattern — provide a way to duplicate objects by cloning them
instead of constructing from scratch."""
import copy

from dask.graph_manipulation import clone


class prototype:
    #a method that, when called on an instance, returns a deep copy of that instance.
    def clone(self):
        #copy.deepcopy(self) creates a new object that is a recursive (deep) copy of self.
        # That means nested mutable attributes are duplicated too, not shared.
        return copy.deepcopy(self)
#defines Car as a subclass of Prototype. Car inherits methods from Prototype, including clone.
class Car(prototype):
    #constructor (initialiser) that runs when you create a Car instance.
    def __init__(self, model, colour):
        #set instance attributes model and color.
        self.model = model
        self.colour = colour
#__str__ is a special method that defines the “informal” string representation of the object
    # — what print(obj) displays.
    def __str__(self):
        #returns a string representation of the Car instance.
        #is an f-string that formats those attributes into a string like "Red Tesla Model S".
        return f"{self.colour} {self.model}"

#client code
#Creates an instance of Car with model="Tesla Model S" and color="Red", and assigns it to the variable car1.
car1 = Car("Tesla Model S", "Red")
#clones car1 by calling its inherited clone() method from Prototype.
#Calls the inherited clone() method on car1.
#Because clone() uses copy.deepcopy(self), car2 becomes a new,
# separate Car instance with the same attribute values as car1.
"""Important: car2 is a distinct object (not the same identity as car1)."""
car2 = car1.clone()
#Modifies the color attribute on the cloned object car2 only.
#Because car2 is a separate object (deep-copied), changing car2.color does not affect car1.color.
car2.colour = "Purple"
print(car1)  # Outputs: Red Tesla Model S
print(car2)  # Outputs: Purple Tesla Model S


