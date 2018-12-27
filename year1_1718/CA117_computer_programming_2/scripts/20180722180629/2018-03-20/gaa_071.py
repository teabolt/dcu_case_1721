#!/usr/bin/env python3

class Score(object):
    # Model a GAA score

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        #self.total_points = points+(goals*3)

    def get_total_points(self):
        return self.goals*3 + self.points

    def greater_than(self, other):
        # other points < self points
        return other.get_total_points() < self.get_total_points()

    def less_than(self, other):
        # self points < other points
        return self.get_total_points() < other.get_total_points()

    def equal_to(self, other):
        # self points = other points
        return self.get_total_points() == other.get_total_points()

def main():
    s1 = Score()
    print(s1.goals, s1.points)
    s2 = Score(points=3)
    s3 = Score(1, 0)
    #s3.points = 4
    print(s2.greater_than(s1))
    print(s1.less_than(s3))
    print(s2.equal_to(s3))

if __name__ == '__main__':
    main()