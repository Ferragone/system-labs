from abc import ABC, abstractmethod

class ShapeCalculator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class CircleCalculator(ShapeCalculator):
    def __init__(self):
        super().__init__()
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        print("Area:", area)

class RectangleCalculator(ShapeCalculator):
    def __init__(self):
        super().__init__()
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))

    def calculate_area(self):
        area = self.length * self.width
        print("Area:", area)

class TriangleCalculator(ShapeCalculator):
    def __init__(self):
        super().__init__()
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area:", area)


shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")

if shape_type == "circle":
    calculator = CircleCalculator()
elif shape_type == "rectangle":
    calculator = RectangleCalculator()
elif shape_type == "triangle":
    calculator = TriangleCalculator()
else:
    print("Invalid shape type")

calculator.calculate_area()