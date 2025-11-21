from abc import ABC, abstractmethod
#product interface
class Vehicle(ABC):#abstract product
    @abstractmethod
    def drive(self):
        pass
#concrete products
class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):#concrete product
    def drive(self):#implementation of abstract method
        return "Riding a bike"

#factory interface
class VehicleFactory(ABC):#abstract factory
    @abstractmethod
    def create_vehicle(self):
        pass
class CarFactory(VehicleFactory):#concrete factory
    def create_vehicle(self):
        return Car()
class BikeFactory(VehicleFactory):#concrete factory
    def create_vehicle(self):
        return Bike()

#client code/test
factory =BikeFactory()#create BikeFactory object
vehicle = factory.create_vehicle()
print(vehicle.drive()) #output: Riding a bike
factory =CarFactory()#create CarFactory object
vehicle = factory.create_vehicle()
print(vehicle.drive())#output: Driving a car

#another way to use factory method without creating separate factory classes
def client_code(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.drive())

#usage
client_code(BikeFactory())
client_code(CarFactory())