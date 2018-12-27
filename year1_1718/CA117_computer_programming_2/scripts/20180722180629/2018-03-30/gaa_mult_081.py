#!/usr/bin/env python3

class Score(object):
    # Model a GAA score

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)

    def get_points(self):
        return self.goals*3 + self.points

    def __eq__(self, other):
        return self.get_points() == other.get_points()

    def __gt__(self, other):
        return self.get_points() > other.get_points()

    def __lt__(self, other):
        return self.get_points() < other.get_points()

    def __ge__(self, other):
        return self.get_points() >= other.get_points()

    def __le__(self, other):
        return self.get_points() <= other.get_points()

    def __add__(self, other):
        goals = self.goals + other.goals
        points = self.points + other.points
        return Score(goals, points)

    def __sub__(self, other):
        goals = self.goals - other.goals
        points = self.points - other.points
        return Score(goals, points)

    def __iadd__(self, other):
        self.goals = self.goals + other.goals
        self.points = self.points + other.points
        return self

    def __isub__(self, other):
        self.goals = self.goals - other.goals
        self.points = self.points - other.points
        return self

    ### extension to multiplication

    def __mul__(self, other):
        goals = self.goals * other
        points = self.points * other
        return Score(goals, points)

    # def __rmul__(self, other):
    #     goals = self.goals * other
    #     points = self.points * other
    #     return Score(goals, points)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        #self.goals = self.goals * other
        self.goals *= other
        #self.points = self.points * other
        self.points *= other
        return self