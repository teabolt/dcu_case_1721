#!/usr/bin/env python3

from math import sqrt

class Point(object):
    # Model a 2D point

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    # method for tests
    def __str__(self):
        return str((self.x, self.y))

class Shape(object):
    # Sequence of connected points (sides)
    # Initial point assumed to connect to the last point

    def __init__(self, points):
        self.points = points

    def sides(self):
        # List of sides' lengths
        points = self.points

        # Edge cases:
        if len(points) == 1: # a point
            return []
        elif len(points) == 2: # a straight line
            return [points[0].distance(points[1])]

        # Points number > 2:
        # Get sides
        left = points # A, B, C
        right = points[1:]+points[:1] # B, C, A (anti-clockwise shift by 1)
        # Associate corresponding left and right points
        spairs = [(j, k) for (j, k) in zip(left, right)]
        # Calculate lenghts
        slens = [side[0].distance(side[1]) for side in spairs]
        return slens

    def perimeter(self):
        # Return the perimeter (sum of sides) of a shape
        return sum(self.sides())

    # method for tests
    def __str__(self):
        return str([str(p) for p in self.points])

class Triangle(Shape):

    def area(self):
        a, b, c = self.sides()
        # Heron's method
        s = (a+b+c)/2
        return sqrt( s*(s-a)*(s-b)*(s-c) )

class Square(Shape):
    
    def area(self):
        a, b, c, d = self.sides()
        return a*a

def main():
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    print(p1, p2, p1.distance(p2), sep='\n')

    shap0 = Shape([])
    print(shap0.sides())

    shap1 = Shape([Point(0,0)])
    print(shap1.sides(), sep='\n')

    shap2 = Shape([Point(0,0), Point(1, 1)])
    print(shap2.sides(), sep='\n')

    shap3 = Shape([Point(0,0), Point(1,0), Point(1,1)])
    print(shap3.sides(), sep='\n')
    print(shap3.perimeter())

    t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
    print(t1.sides())
    print(t1.perimeter())
    print(t1.area())

    t2 = Triangle([Point(0,0), Point(4,0), Point(4, 3)])
    print(t2.sides())
    print(t2.perimeter())
    print(t2.area())

    s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
    print(s1.sides())
    print(s1.perimeter())
    print(s1.area())

if __name__ == '__main__':
    main()