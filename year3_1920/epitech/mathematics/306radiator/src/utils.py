#!/usr/bin/env python3

import sys
from decimal import localcontext, Decimal, ROUND_HALF_UP

from constants import ERROR_EXIT_CODE, HELP_MESSAGE


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
    n, ir, jr = argv[:3]
    n = _to_int(n)
    if n <= 2:
        error_exit('Invalid room size. Got %d' % n)
    ir = _to_int(ir)
    _is_valid_coordinate(ir, n)
    jr = _to_int(jr)
    _is_valid_coordinate(jr, n)
    if len(argv) == 5:
        i, j = argv[3:]
        i = _to_int(i)
        _is_valid_coordinate(i, n)
        j = _to_int(j)
        _is_valid_coordinate(j, n)
        return n, ir, jr, i, j
    else:
        return n, ir, jr


def _to_int(x):
    try:
        return int(x)
    except ValueError:
        error_exit('Could not convert argument to integer: %s' % x)


def _is_valid_coordinate(x, n):
    if not is_inside_walls(x, n):
        error_exit('Coordinate argument is invalid. Got: %d' % x)


def is_inside_walls(x, n):
    return 1 <= x <= n-2

def is_inside_bounds(x, n):
    return 0 <= x <= n-1


def round_up(x):
    # https://stackoverflow.com/a/33019948 for https://stackoverflow.com/questions/33019698/how-to-properly-round-up-half-float-numbers-in-python
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        n = Decimal(x)
        return str(n.quantize(Decimal('1.0')))
