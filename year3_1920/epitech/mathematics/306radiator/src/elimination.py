#!/usr/bin/env python3

"""Gaussian elimination algorithm implementation."""


import time
from utils import error_exit


# this is taken from
# https://martin-thoma.com/solving-linear-equations-with-gaussian-elimination/
#
def gauss(AugMat):
    """
    This function solves the equation AX=Y matrix equation.
    Input is a (n+1)*n 2D list in the form of an augmented matrix.
    The last column is the right side of the matrix equation (the Y).
    Entries are instances of Fraction.

    The result is X, a vector (list) with n entries of Fraction.
    """
    n = len(AugMat)

    t1 = time.time()
    for i in range(0, n):
        if (time.time() - t1) > 5:
            error_exit('Gaussian elimination is taking a long time! Force-stopping ...')
        maxr = _max_row(AugMat, i)
        _swap_rows(AugMat, i, maxr)
        _zero_below(AugMat, i)
    return _back_solve(AugMat)


def _max_row(Mat, i):
    """Search for the maximum row in the i column of matrix Mat."""
    n = len(Mat)
    e = abs(Mat[i][i])
    maxr = i
    for k in range(i + 1, n):
        if abs(Mat[k][i]) > e:
            e = abs(Mat[k][i])
            maxr = k
    return maxr


def _swap_rows(Mat, i, j):
    """Swap rows i and j in the matrix Mat."""
    n = len(Mat)
    for k in range(i, n + 1):
        tmp = Mat[j][k]
        Mat[j][k] = Mat[i][k]
        Mat[i][k] = tmp


def _zero_below(Mat, i):
    """Make rows below row i zero in current column of matrix Mat."""
    n = len(Mat)
    for k in range(i + 1, n):
        c = -Mat[k][i] / Mat[i][i]
        for j in range(i, n + 1):
            if i == j:
                Mat[k][j] = 0
            else:
                Mat[k][j] += c * Mat[i][j]


def _back_solve(Mat):
    """Solve the upper triangular matrix 'Mat' by back-substitution."""
    n = len(Mat)
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = Mat[i][n] / Mat[i][i]
        for k in range(i - 1, -1, -1):
            Mat[k][n] -= Mat[k][i] * x[i]
    return x
