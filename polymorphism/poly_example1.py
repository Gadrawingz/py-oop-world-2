"""
Polymorphism:
-It is another important concept of OOP.
-It simply means more than one form.
-The same entity (method or operator or object) can perform
different operations in different scenarios.
"""

class Polygon:
    # method to render a shape
    def render(self):
        print("For rendering Polygon...")


class Square(Polygon):
    # Renders Square
    def render(self):
        print("For rendering Square...")


class Circle(Polygon):
    # renders circle
    def render(self):
        print("For rendering Circle...")


# create an object of Square
square1 = Square()
square1.render()

# create an object of Circle
circle1 = Circle()
circle1.render()
