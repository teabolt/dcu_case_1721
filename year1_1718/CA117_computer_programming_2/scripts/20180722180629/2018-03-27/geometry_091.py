#!/usr/bin/env python3

class Point(object):
    # Model for a 2D point

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    def distance(self, other):
        return ( (self.x-other.x)**2 + (self.y-other.y)**2 )**0.5

class Shape(object):
    # Sequence of connected points(sides)
    # Initial point is assumed to connect to the last point

    def __init__(self, points):
        self.points = points

    def sides(self):
        # Lengths of all the shape's sides
        points = self.points
        # i = len(points)-1
        # while 0 < i:
        #     p2 = points[i]
        #     p1 = points[i-1]
        #     print(p1, p2)
        #     i -= 1


    def perimeter(self):
        pass

class Triangle(Shape):

    def area(self):
        pass

class Square(Shape):
    
    def area(self):
        pass

def main():
    p1 = Point(0, 0)
    p2 = Point(2, 2)
    #print(p1.distance(p2))

    shap1 = Shape([p1, p2, Point(3, 4)])
    print(shap1.points)
    print(shap1.sides())

if __name__ == '__main__':
    main()