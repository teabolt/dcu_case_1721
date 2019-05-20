#!/usr/bin/env python3

import math


class Vector(list):
    pass


def scale(c, v):
    return Vector([c*x for x in v])


def inner_product(u, v):
    return sum([x*y for x, y in zip(u, v)])


def length(v):
    return math.sqrt(sum([x**2 for x in v]))
