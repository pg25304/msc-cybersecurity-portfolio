from abc import ABC, abstractmethod
# Car abstract/Interface
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass
# Concrete Car classes
class Sedan(Car):
    def drive(self):
        return "Driving a Sedan"
class SUV(Car):
    def drive(self):
        return "Driving an SUV"
class Hatchback(Car):
    def drive(self):
        return "Driving a Hatchback"
# Car Factory abstract/interface
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass
# Concrete Car Factory classes
class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()
class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()
class HatchbackFactory(CarFactory):
    def create_car(self):
        return Hatchback()
# Client code/test
def client_code(factory: CarFactory):
    car = factory.create_car()
    print(car.drive())
# Usage
client_code(SedanFactory())
client_code(SUVFactory())
client_code(HatchbackFactory())

