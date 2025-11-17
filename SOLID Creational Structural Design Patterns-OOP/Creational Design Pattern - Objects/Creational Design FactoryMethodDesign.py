"""An abstract class is like a template or blueprint for other classes.
It defines what methods a subclass must implement, but doesn’t provide
full implementations itself.ABC stands for Abstract Base Class.
It’s part of Python’s built-in abc module, which lets you define abstract classes —
classes that are meant to be  templates and cannot be instantiated (create object directly from a class) directly."""
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
"""Car and Bike both inherit from Vehicle and provide their own implementation of the abstract drive() method.
Now they are concrete classes — you can create instances of them because they have implemented 
everything required by the base class."""
class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

#client code/test
car = Car()
print(car.drive())
bike = Bike()
print(bike.drive())
# v=Vehicle() Error: Can't instantiate abstract class
#Using factories to create vehicles
print("Factory (Factory Method / Simple Factory) creates one product type and hides concrete class selection.")
factory = CarFactory()
vehicle = factory.create_vehicle()
print(vehicle.drive())
print("############################################")
factory = BikeFactory()
vehicle = factory.create_vehicle()
print(vehicle.drive())
