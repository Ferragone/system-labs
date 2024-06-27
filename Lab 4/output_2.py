from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self, *args):
        pass

class Square(Shape):
    def area(self, side):
        return side ** 2

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


square = Square()
print("Area of square:", square.area(5))

circle = Circle()
print("Area of circle:", circle.area(3))