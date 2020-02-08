#!/usr/bin/env python3

"""Utility functions."""

import sys
from constants import (
    ERROR_EXIT_CODE,
    HELP_MESSAGE,
    GRAIN_NAMES,
)


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
    ret = list(map(_to_int, ret))
    if not all(0 <= x for x in ret):
        error_exit('Arguments contain a negative number: {}'.format(ret))
    n1, n2, n3, n4, po, pw, pc, pb, ps = ret
    return n1, n2, n3, n4, po, pw, pc, pb, ps


def _to_int(x):
    try:
        return int(x)
    except ValueError:
        error_exit('Could not convert argument to integer: %s' % x)


def print_produce(units_to_produce, unit_prices):
    """Print the units and price for each resource."""
    for i, (units, price) in enumerate(zip(units_to_produce, unit_prices)):
        if units == 0:
            precision_spec = '{}'
        else:
            precision_spec = '{:.2f}'
        format_spec = '{}: ' + precision_spec + ' units at ${}/unit'
        print(format_spec.format(GRAIN_NAMES[i].capitalize(), units, price))


def total_sales(units_to_produce, unit_prices):
    """Calculate the total production value from the number of units and individual unit prices."""
    total = 0
    for units, price in zip(units_to_produce, unit_prices):
        total += units * price
    return total


def isIncludedNegative(lst):
    return bool(sum(1 for i in lst if i < 0))
