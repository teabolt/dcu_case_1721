#!/usr/bin/env python3

from math import sqrt

class Point(object):
    # Model a point in 2D space

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        # Reflect point through the origin
        self.x = -self.x
        self.y = -self.y

    def distance(self, other):
        # Return the distance between two points
        return sqrt( (other.x-self.x)**2 + (other.y-self.y)**2 )

def main():
    p1 = Point()
    print(p1.x)
    p2 = Point(y=3)
    print(p2.y)
    p3 = Point(-4, 3)
    p3.reflect()
    print(p3.x, p3.y)
    p4 = Point(1, 1)
    print(p1.distance(p2))
    print(p3.distance(p3))
    print(p1.distance(p4))

if __name__ == '__main__':
    main()