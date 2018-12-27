#!/usr/bin/env python3

class Weight(object):
    # Model a weight

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    @classmethod
    def from_ounces(cls, ounces):
        pounds, ounces = divmod(ounces, Weight.OUNCES_PER_POUND)
        return Weight(pounds, ounces)

    def __str__(self):
        return '{} pound(s) and {} ounce(s)'.format(self.pounds, self.ounces)

    def to_ounces(self):
        return self.pounds*Weight.OUNCES_PER_POUND + self.ounces

    def __eq__(self, other):
        return self.to_ounces() == other.to_ounces()

    def __lt__(self, other):
        return self.to_ounces() < other.to_ounces()

    def __ge__(self, other):
        return self.to_ounces() >= other.to_ounces()

    def __add__(self, other):
        pounds = self.pounds + other.pounds
        ounces = self.ounces + other.ounces
        return Weight(pounds, ounces)

    def __iadd__(self, other):
        self.pounds += other.pounds
        self.ounces += other.ounces
        return self

    def __mul__(self, other):
        pounds = self.pounds * other
        ounces = self.ounces * other
        return Weight(pounds, ounces)