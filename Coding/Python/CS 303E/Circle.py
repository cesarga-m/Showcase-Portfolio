import math


class Circle:
    def __init__(self, rad=1):
        self . radius = rad

    def getRadius(self):    # getter
        return self . radius

    def setRadius(self, rad):   # setter
        self . radius = rad

    def getPerimeter(self):
        return 2 * math . pi * self . radius

    def getArea(self):
        return math . pi * (self . radius ** 2)
