import math

class Shape:
    def area(self):
        pass
    
    def parameter(self):
        pass
    def circumfrance(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def parameter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ^ 2)

    def circumfrance(self):
        return 2 * math.pi * self.radius
    
myRectangle = Rectangle(5, 4)
myCircle = Circle(20)
    
print(myRectangle.area())
print(myRectangle.parameter())
print(myCircle.area())
print(myCircle.circumfrance())