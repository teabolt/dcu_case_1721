#!/usr/bin/env python3

class Point(object):
    # Model a 2D point

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)

    def midpoint(self, other):
        x = (self.x+other.x) / 2
        y = (self.y+other.y) / 2
        return Point(x, y)

class Circle(object):
    # Model a 2D circle

    def __init__(self, centre=None, radius=0):
        if centre == None:
            centre = Point(0, 0)
        self.radius = radius
        self.centre = centre

    def __str__(self):
        a = []
        a.append('Centre: {}'.format(self.centre))
        a.append('Radius: {}'.format(self.radius))
        return '\n'.join(a)

    def __add__(self, other):
        centre = self.centre.midpoint(other.centre)
        radius = self.radius + other.radius
        return Circle(centre, radius)

def main():
    # Tests
    p1 = Point()
    p2 = Point(4, 6)
    #print(p1.midpoint(p2))

    c1 = Circle(p1, radius=1)
    c2 = Circle(p2, radius=10)
    print(c1)
    print(c2)
    c3 = c1 + c2
    print(c3)

if __name__ == '__main__':
    main()