""" 
     Create three classes:
     1) Rectangle 
     2) Square 
     3) Cube 
    
     a) Create constructors (__init__)
     b) methods calculating the surface_area of a square, rectangle, cube
     c) a method calculating the volume of the cube

     Consider how you can use inheritance to do this so that you don't repeat the code
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


class Cube(Square):
    def count_surface_area(self):
        return super().count_surface_area() * 6

    def count_volume(self):
        return super().count_surface_area() * self.height


cube = Cube(2)

print(cube.count_volume())
