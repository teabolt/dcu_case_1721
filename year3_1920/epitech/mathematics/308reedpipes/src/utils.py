#!/usr/bin/env python3

"""Utility functions."""

import sys
from constants import (
    ERROR_EXIT_CODE,
    HELP_MESSAGE
)


def new_array(n, value=0):
    return [value] * n


def get_help():
    return HELP_MESSAGE


def error_exit(message):
    print(message, file=sys.stderr)
    sys.exit(ERROR_EXIT_CODE)


def parse_args(argv):
    """
    Extract program arguments from the argument vector.
    Note that argv must not include the program name.
    """
    ret = argv[1:]
    ret = list(map(_to_float, ret))
    ret[-1] = _to_int(ret[-1])
    if not all(0 <= x for x in ret):
        error_exit('Arguments contain a negative number: {}'.format(ret))
    r0, r5, r10, r15, r20, n = ret
    radii = [r0, r5, r10, r15, r20]
    if n < 5:
        error_exit('Invalid number of points to display: %d (need at least 5)' % n)
    if not all(0 < x for x in radii):
        error_exit('Radius must be non-zero. Got radii {} (will not manufacture a pipe with no opening)'.format(radii))
    return r0, r5, r10, r15, r20, n


def _to_float(x):
    try:
        return float(x)
    except ValueError:
        error_exit('Could not convert argument to float: %s' % x)


def _to_int(x):
    try:
        return int(x)
    except ValueError:
        error_exit('Could not convert argument to integer: %s' % x)


def print_vec(vec):
    print('vector result: ', end='')
    nums = (format(x, '.1f') for x in vec)
    print('[', end='')
    print(', '.join(nums), end='')
    print(']', end='')
    print()


def print_interpolation(interpolation):
    for abscissa, radius in interpolation:
        print('abscissa: {:.1f} cm\tradius: {:.1f} cm'.format(abscissa, radius))
