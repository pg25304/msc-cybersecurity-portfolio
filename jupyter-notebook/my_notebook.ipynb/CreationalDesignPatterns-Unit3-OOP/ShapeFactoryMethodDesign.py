from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def draw(self):
        return f"Drawing a rectangle with width {self.width} and length {self.length}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def draw(self):
        return f"Drawing a square with side {self.side}"

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

class RectangleFactory(ShapeFactory):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def create_shape(self):
        return Rectangle(self.width, self.length)

class SquareFactory(ShapeFactory):
    def __init__(self, side):
        self.side = side

    def create_shape(self):
        return Square(self.side)

# Client code/test
factory = RectangleFactory(5,7)
rectangle = factory.create_shape()
print(rectangle.draw())

factory = SquareFactory(5)
square = factory.create_shape()
print(square.draw())

