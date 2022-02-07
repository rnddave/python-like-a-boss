"""
Geometry inheritance

create 4x class [Polygon], [Triangle], [Rectangle], [Square]

The [Triangle] and [Rectangle] class should be subclasses of [Polygon] and [Square] should be a subclass of [Rectagle] 


Your [Polygon] class should raise a [NotimplementedError] when the [get_area()] and [get_sides()] methods are called. 
However it should correctly return the perimeter of the polygon when [get_perimeter()] is called. Treat [Polygon] class as an *abstract* class. 

Your [Triangle] class should have a constructor that takes 3 arguments, which will be the len of the 3x side. 
You may assume that the sides passed will always for a triangle. 

Your [Rectangle] class should have a constructor that takes 2 arguments, which will be the [width] and [height] of the [Rectangle]

Your [Square] class should have a constructor that takes 1 argument which will be the length of each side of the [Square]

Your [Triange] and [Rectangle] classes should both implement the following methods: 
-- [get_sides()] = return a list containing the lengths of the sides of the shape
-- [get_area()] = area of the polygon

Your [Square] class should only have an implementation for its constructor, and rely on the [Rectangle] superclass for implementations of [get_sides()] and [get_area()]

"""

import math


class Polygon:
    def get_sides(self):
        raise NotImplementedError

    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):
    # Write your code here.
    pass


class Rectangle(Polygon):
    # Write your code here.
    pass


class Square(Rectangle):
    # Write your code here.
    pass


# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height
