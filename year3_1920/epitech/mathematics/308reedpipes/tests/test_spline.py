#!/usr/bin/env python3

"""Unit tests for spline interpolation."""

import sys
sys.path.append('./src')
import unittest
from src.spline import interpolate


class TestSplineInterpolation(unittest.TestCase):

    DUMMY_POINTS = [(0, 1), (5, 2), (10, 3), (15, 4), (20, 5)]
    NUM_POINTS = 5

    def test_a(self):
        self.assertEqual(interpolate([(0, 1.5), (5, 2), (10, 2), (15, 2), (20, 5)], 11),
                         ([0, 0, 0, 0.2, 0],
                          [(0, 1.5), (2, 1.7), (4, 1.9), (6, 2.1), (8, 2.1), (10, 2.0),
                           (12, 1.8), (14, 1.8), (16, 2.4), (18, 3.5), (20, 5)]))

    def test_b(self):
        self.assertEqual(interpolate([(0, 2), (5, 3), (10, 2), (15, 4), (20, 5)], 13),
                         ([0, -0.2, 0.3, -0.1, 0],
                          [(0, 2), (1.7, 2.6), (3.3, 3.0), (5.0, 3.0), (6.7, 2.6), (8.3, 2.2),
                           (10, 2.0), (11.7, 2.4), (13.3, 3.2), (15, 4), (16.7, 4.5), (18.3, 4.8), (20, 5)]))

    def test_no_interpolation(self):
        self.assertEqual(interpolate(self.DUMMY_POINTS, self.NUM_POINTS),
                         ([0, 0, 0, 0, 0], # FIXME
                          self.DUMMY_POINTS))

    def test_invalid_num(self):
        # zero
        with self.assertRaises(ValueError):
            interpolate(self.DUMMY_POINTS, 0)

        # negative
        with self.assertRaises(ValueError):
            interpolate(self.DUMMY_POINTS, -1)

        # less than number of given points
        with self.assertRaises(ValueError):
            interpolate(self.DUMMY_POINTS, 4)

        # bad type
        with self.assertRaises(TypeError):
            interpolate(self.DUMMY_POINTS, '10')
        with self.assertRaises(TypeError):
            interpolate(self.DUMMY_POINTS, 10.5)

    def test_invalid_points(self):
        # bad type
        with self.assertRaises(TypeError):
            # must be list of tuples
            interpolate((2, 3), self.NUM_POINTS)

        # empty list
        with self.assertRaises(ValueError):
            # must be an iterable of tuples
            interpolate([], self.NUM_POINTS)

        # bad contents
        with self.assertRaises(ValueError):
            # must be list of tuples
            interpolate([3, None], self.NUM_POINTS)
        with self.assertRaises(ValueError):
            # tuples must have float values
            interpolate([('2', 3)], self.NUM_POINTS)

        # TODO: must have at least 2 points for interpolation to work?


if __name__ == '__main__':
    unittest.main()
