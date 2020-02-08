#!/usr/bin/env python3

"""Unchanging program values."""


ERROR_EXIT_CODE = 84


HELP_MESSAGE = """USAGE
    ./307multigrains n1 n2 n3 n4 po pw pc pb ps

DESCRIPTION
    n1      number of tons of fertilizer F1
    n2      number of tons of fertilizer F2
    n3      number of tons of fertilizer F3
    n4      number of tons of fertilizer F4
    po      price of one unit of oat
    pw      price of one unit of wheat
    pc      price of one unit of corn
    pb      price of one unit of barley
    ps      price of one unit of soy"""


GRAIN_NAMES = ['oat', 'wheat', 'corn', 'barley', 'soy']


# The matrix table for simplex method
# n1, n2, n3, n4, n5, u, v, w, x, f(x)
# Note that the elements with n is the number of units,
# u, v, w, x are the slack variables,
# and f(x) means objective function
SIMPLEX_TABLE = [
    [1, 0, 1, 0, 2, 1, 0, 0, 0, 0],  # for F1
    [1, 2, 0, 1, 0, 0, 1, 0, 0, 0],  # for F2
    [2, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # for F3
    [0, 0, 3, 1, 2, 0, 0, 0, 1, 0],  # for F4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]   # for price of each unit
]
