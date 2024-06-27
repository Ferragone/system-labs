from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        return 0.5 * self.base * self.height


shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")

if shape_type == "circle":
    shape = Circle()
elif shape_type == "rectangle":
    shape = Rectangle()
elif shape_type == "triangle":
    shape = Triangle()
else:
    print("Invalid shape type")

area = shape.calculate_area()
print("Area:", area)