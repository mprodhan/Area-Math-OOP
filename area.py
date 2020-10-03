import math

class Area():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Square(Area):
    def __init__(self, side):
        self.side = side

    def square_area(self):
        return self.side**2

class Rectangle(Area):
    def area(self):
        return self.length*self.width

square1 = Area(2,2)
sqaure2 = Square(2)
rectangle1 = Rectangle(2,3)

print(square1.area())
print(sqaure2.square_area())
print(rectangle1.area())
