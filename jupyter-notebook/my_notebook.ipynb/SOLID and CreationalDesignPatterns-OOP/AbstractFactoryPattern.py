#Product abstracts
from abc import ABC, abstractmethod
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass
class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass
#Concrete products
class ModernChair(Chair):
    def sit_on(self):
        return "Sit on a modern chair"

class ModernSofa(Sofa):
    def lie_on(self):
        return "ley on a modern sofa"
#Abstract factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass
    @abstractmethod
    def create_sofa(self0):
        pass
#concrete  Factory
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    def create_sofa(self0):
        return ModernSofa()


#Client code
print("Abstract Factory creates families of related products (multiple product types that belong together)")
factory = ModernFurnitureFactory()
chair = factory.create_chair()
sofa = factory.create_sofa()
print(chair.sit_on())
print(sofa.lie_on())