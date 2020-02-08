#!/usr/bin/env python3

import logging
from fractions import Fraction

from constants import POWER_AT_RADIATOR
from utils import (
    is_inside_walls,
    is_inside_bounds,
    round_up,
)
from elimination import (
    gauss,
)


def generate_equations(n, ir, jr):
    """Get A and Y matrices from the size n and point of the radiator."""
    A = _Matrix(n**2)
    Y = _SparseMatrix(n**2)
    for num in range(n**2):
        logging.info('Calculating row number %d' % num)
        left_coeffs, right_coeffs = _get_equation_coefficients(num, n, ir, jr)
        A.row_insert(left_coeffs, num)
        Y.row_insert(right_coeffs, num)
    return A, Y


def _get_equation_coefficients(num, n, ir, jr):
    """Return coefficients of Left Hand Side and Right Hand Side (the result)."""
    left = [0] * n**2
    i, j = index_to_coordinates(num, n)
    if not (is_inside_walls(i, n) and is_inside_walls(j, n)):
        # wall
        left[num] = 1
    else:
        # not a wall
        # FIXME: equation is hard-coded and does not use the H variable
        _add_term(left, i-1, j, n, 4)  # x minus
        _add_term(left, i, j-1, n, 4)  # y_minus
        _add_term(left, i, j, n, -16)  # x_y
        _add_term(left, i+1, j, n, 4)  # x_plus
        _add_term(left, i, j+1, n, 4)  # y_plus

    if i == ir and j == jr:
        # at radiator
        right = [POWER_AT_RADIATOR]
    else:
        # null point
        right = [0]

    return left, right


def _add_term(coeffs, i, j, n, coeff):
    if is_inside_bounds(i, n) and is_inside_bounds(j, n):
        # FIXME: is the if statement needed?
        # negative indices will not appear because the points considered are inside walls
        num = coordinates_to_index(i, j, n)
        coeffs[num] = coeff


def gaussian_solve(A, Y):
    """Solve AX=Y for X."""
    X = _SparseMatrix(len(A[0]))

    n = Y.size
    M = [[0 for j in range(n+1)] for i in range(n)]
    for i in range(0, n):
        row = map(Fraction, A.get_2d()[i])
        for j, el in enumerate(row):
            M[i][j] = el
    for i in range(0, n):
        augmentedRow = list(map(Fraction, Y.get_2d()[i]))
        M[i][n] = augmentedRow[0]

    _X = gauss(M)

    for i, e in enumerate(_X):
        x = e.numerator / e.denominator
        X.row_insert([x], i)
    return X


def index_to_coordinates(num, n):
    i, j = (num // n, num % n)
    logging.debug('Converted index {} to coordinates {}, {}'.format(num, i, j))
    return i, j


def coordinates_to_index(i, j, n):
    num = i*n + j
    logging.debug('Converted coordinates {}, {} to index {}'.format(i, j, num))
    return num


class _Matrix(object):
    """2D matrix."""

    def __init__(self, size, data=None):
        self.size = size
        if data is None:
            self._data = [[0 for _ in range(size)] for _ in range(size)]
        else:
            self._data = data
        logging.info('Initial matrix data: {}'.format(self._data))

    def row_insert(self, row, index):
        logging.info('Adding to matrix the row {}'.format(row))
        self._data[index] = row

    def get_2d(self):
        return self._data

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self._data)

    def __getitem__(self, key):
        return self._data[key]


class _SparseMatrix(_Matrix):
    """1D matrix full of zeroes."""

    def __init__(self, size):
        self.size = size
        self._data = {}
        logging.info('Initial matrix data: {}'.format(self._data))

    def row_insert(self, row, index):
        logging.info('Adding to matrix the row {}'.format(row))
        if row == [0]:
            pass
        else:
            self._data[index] = row

    def get_2d(self):
        mat = [[0] for _ in range(self.size)]
        for index, row in self._data.items():
            mat[index] = row
        return mat

    def get_colvect(self):
        mat = [[0] for _ in range(self.size)]
        for index, row in self._data.items():
            mat[index], = row
        return mat

    def __str__(self):
        mat = [[0] for _ in range(self.size)]
        for index, row in self._data.items():
            mat[index] = row
            # str(round(x, 1))
        return '\n'.join('\t'.join(map(lambda x: round_up(x), row)) for row in mat)

    def __getitem__(self, key):
        return self._data[key] if key in self._data else 0
