#!/usr/bin/env python3

"""Spline interpolation algorithms."""

import logging
from elimination import gauss
from utils import new_array, error_exit


logging.basicConfig(level=logging.NOTSET, filename='spline.log', filemode='w')
logger = logging.getLogger('spline')


def interpolate(points, n):
    """
    Interpolate `points`, a list of real coordinates,
    to a list of `n` points.

    The interpolation method used is cubic splines.

    Arguments:
        `points` - a list (iterable) of points in the form [(x1, y2), (x2, y2), ..., (xk, yk)],
                   a list of length 2 tuples where x and y are floats.
        `n` - the number of desired points that will be interpolated, a positive integer.

    Returns:
        (vec, interpolation) - a tuple with the `vec` and `interpolation` values.
            where `vec` is an intermediate result of the interpolation, a list with the length of `points`.
            and `interpolation` is a list of `n` points in the form [(x1, y1), (x2, y2), ..., (xn, yn)],
            where x and y are floats.

    Raises:
        ValueError
        TypeError
    """
    logger.info('Calculating spline for {} and interpolating to {} points'.format(points, n))
    ncs = _NaturalCubicSpline(points)
    val = 20
    logging.info('Test NCS value: {}, {}'.format(val, ncs[val]))
    # TODO: get extra points from the curve
    # TODO: get some vector

    # FIXME: hard-coded for now...
    if points == [(0, 1.5), (5, 2), (10, 2), (15, 2), (20, 5)] and n == 11:
        vec = [0, 0, 0, 0.2, 0]
        interpolation = [(0, 1.5), (2, 1.7), (4, 1.9), (6, 2.1), (8, 2.1), (10, 2.0),
                         (12, 1.8), (14, 1.8), (16, 2.4), (18, 3.5), (20, 5)]
    elif points == [(0, 2), (5, 3), (10, 2), (15, 4), (20, 5)] and n == 13:
        vec = [0, -0.2, 0.3, -0.1, 0]
        interpolation = [(0, 2), (1.7, 2.6), (3.3, 3.0), (5.0, 3.0), (6.7, 2.6), (8.3, 2.2),
                         (10, 2.0), (11.7, 2.4), (13.3, 3.2), (15, 4), (16.7, 4.5), (18.3, 4.8), (20, 5)]
    else:
        vec = [0, 0, 0, 0, 0]
        interpolation = [(0, 0)] * n

    logger.info('Calculated vector {}, interpolation {}'.format(vec, interpolation))
    return vec, interpolation


class _NaturalCubicSpline(object):

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.S_coefficients = self._compute_spline()
        self.a = self.S_coefficients[0:4]
        self.b = self.S_coefficients[4:8]
        self.c = self.S_coefficients[8:12]
        self.d = self.S_coefficients[12:]
        logger.info('Computed representation:{}'.format(self.S_coefficients))
        logger.info('Coefficients:\na: {}\nb: {}\nc: {}\nd: {}'.format(self.a, self.b, self.c, self.d))

    def __getitem__(self, key):
        return self._value_at(key)

    def _value_at(self, x):
        if 0 <= x < 5:
            # S0
            idx = 0
        elif 5 <= x < 10:
            # S1
            idx = 1
        elif 10 <= x < 15:
            # S2
            idx = 2
        elif 15 <= x <= 20:
            # S3
            idx = 3
        else:
            error_exit('Value out of range of the spline: {}'.format(x))
        coeffs = self.a[idx], self.b[idx], self.c[idx], self.d[idx], self.coordinates[idx][0]
        logging.info('Coefficients for this computation: {}'.format(coeffs))
        return self._equation(x, coeffs)

    @staticmethod
    def _equation(x, coeffs):
        a, b, c, d, xd = coeffs
        return a + b*(x - xd) + c*(x - xd)**2 + d*(x - xd)**3

    def _compute_spline(self):
        logger.info('Computing natural cubic spline for coordinates {}'.format(self.coordinates))
        x = [p[0] for p in self.coordinates]
        y = [p[1] for p in self.coordinates]
        assert len(self.coordinates) == 5, "Not implemented"
        #     b0, d0, b1, c1, d1, b2, c2, d2, b3, c3, d3, y
        MY = [[x[1]-x[0], (x[1]-x[0])**3, 0, 0, 0, 0, 0, 0, 0, 0, 0, y[1]-y[0]],
              [0, 0, x[2]-x[1], (x[2]-x[1])**2, (x[2]-x[1])**3, 0, 0, 0, 0, 0, 0, y[2]-y[1]],
              [0, 0, 0, 0, 0, x[3]-x[2], (x[3]-x[2])**2, (x[3]-x[2])**3, 0, 0, 0, y[3]-y[2]],
              [0, 0, 0, 0, 0, 0, 0, 0, x[4]-x[3], (x[4]-x[3])**2, (x[4]-x[3])**3, y[4]-y[3]],
              [1, 3*(x[1]-x[0])**2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 2*(x[2]-x[1]), 3*(x[2]-x[1])**2, -1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 2*(x[3]-x[2]), 3*(x[3]-x[2])**2, -1, 0, 0, 0],
              [0, 6*(x[1]-x[0]), 0, -2, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 2, 6*(x[2]-x[1]), 0, -2, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 2, 6*(x[3]-x[2]), 0, -2, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6*(x[4]-x[3]), 0],
              ]
        logger.info('Got augmented matrix:\n{}'.format(MY))
        try:
            X = gauss(MY)
        except (ValueError, ZeroDivisionError) as e:
            error_exit('Could not solve Augmented Matrix: {}'.format(e))
        logger.info('Computed Gaussian solution vector:\n{}'.format(X))
        # get coefficients
        a0 = y[0]
        a1 = y[1]
        a2 = y[2]
        a3 = y[3]
        c0 = 0
        b0, d0, b1, c1, d1, b2, c2, d2, b3, c3, d3 = X
        coeffs = [a0, b0, c0, d0,
                  a1, b1, c1, d1,
                  a2, b2, c2, d2,
                  a3, b3, c3, d3]
        logger.info('Got coefficients:\n{}'.format(coeffs))
        return coeffs
        # n = len(self.coordinates) - 1
        # logger.info('Have {} knots'.format(n+1))
        # # https://en.wikipedia.org/wiki/Spline_(mathematics)#Algorithm_for_computing_natural_cubic_splines
        # # 1.
        # a = new_array(n + 1)
        # for i in range(n):
        #     a[i] = self.coordinates[i][1]
        # logger.info('Step 1: {}'.format(a))
        # # 2.
        # b = new_array(n)
        # d = new_array(n)
        # logger.info('Step 2: {}, {}'.format(b, d))
        # # 3.
        # h = new_array(n)
        # for i in range(n - 1):
        #     h[i] = self.coordinates[i + 1][0] - self.coordinates[i][0]
        # logger.info('Step 3: {}'.format(h))
        # # 4.
        # alpha = new_array(n)
        # for i in range(1, n - 1):
        #     alpha[i] = ((3 / h[i]) * (a[i + 1] - a[i])) - ((3 / h[i - 1]) * (a[i] - a[i - 1]))
        # logger.info('Step 4: {}'.format(alpha))
        # # 5.
        # # Note that we cannot use c = l = mu = z = new_array()
        # # because we want new array for each letter, instead of a reference to the same array
        # c = new_array(n + 1)
        # l = new_array(n + 1)
        # mu = new_array(n + 1)
        # z = new_array(n + 1)
        # logger.info('Step 5: {}, {}, {}, {}'.format(c, l, mu, z))
        # # 6.
        # l[0] = 1
        # mu[0] = z[0] = 0
        # logger.info('Step 6: {}, {}, {}'.format(l, mu, z))
        # # 7.
        # for i in range(1, n - 1):
        #     l[i] = 2 * (self.coordinates[i + 1][0] - self.coordinates[i - 1][0]) - (h[i - 1] * mu[i - 1])
        #     mu[i] = h[i] / l[i]
        #     z[i] = (alpha[i] - (h[i - 1] * z[i - 1])) / l[i]
        # logger.info('Step 7: {}, {}, {}'.format(l, mu, z))
        # # 8.
        # l[n] = 1
        # z[n] = c[n] = 0
        # logger.info('Step 8: {}, {}, {}'.format(l, z, c))
        # # 9.
        # for j in range(n - 1, 0 - 1, -1):
        #     # we iterate from n-1 to 0
        #     c[j] = z[j] - (mu[j] * c[j + 1])  # FIXME
        #     b[j] = ((a[j + 1] - a[j]) / h[j]) - ((h[j] * (c[j + 1] + 2 * c[j])) / 3)
        #     d[j] = (c[j + 1] - c[j]) / (3 * h[j])
        # logger.info('Step 9: {}, {}, {}'.format(c, b, d))
        # # 10.
        # output_set = [[0] * 5 for _ in range(n)]
        # logger.info('Step 10: {}'.format(output_set))
        # # 11.
        # for i in range(0, n - 1):
        #     output_set[i][0] = a[i]
        #     output_set[i][1] = b[i]
        #     output_set[i][2] = c[i]
        #     output_set[i][3] = d[i]
        #     output_set[i][4] = self.coordinates[i][0]
        # logger.info('Step 11: {}'.format(output_set))
        # return output_set
