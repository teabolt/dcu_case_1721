#!/usr/bin/env python3

from math import sqrt

class Point(object):
    # Model a 2D point with coordinates (x,y).

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __str__(self):
        return str('({:.1f}, {:.1f})'.format(self.x, self.y))

    def distance(self, other):
        return sqrt( (self.x-other.x)**2 + (self.y-other.y)**2 )

class Segment(object):
    # Model a line segment

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        x = (self.p1.x+self.p2.x) / 2
        y = (self.p1.y+self.p2.y) / 2
        return Point(x, y)

    def length(self):
        return self.p1.distance(self.p2)

class Circle(object):
    # Model a circle
    
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def overlaps(self, other):
        # Return True if self overlaps with other circle
        # Touching is not overlapping
        c_dist = Segment(self.centre, other.centre).length()
        r_dist = self.radius+other.radius
        return c_dist < r_dist
        
def main():
    p1 = Point()
    print(p1)
    p2 = Point(1, 1)
    print(p1)
    print(p1.distance(p2))

    s1 = Segment(p1, p2)
    print(s1.midpoint())
    print(s1.length())

    c1 = Circle(p1, 1)
    print(c1.radius)
    c2 = Circle(Point(100, 100), 1)
    print(c2.centre)
    print(c1.overlaps(c2))

if __name__ == '__main__':
    main()