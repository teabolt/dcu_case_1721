#!/usr/bin/env python3

"""The simplex optimization algorithm."""

import sys

from constants import SIMPLEX_TABLE
from utils import isIncludedNegative


def optimize(fertilizer_tons, unit_prices):
    """Compute the number of units to produce for each grain,
    using the simplex method.
    fertilizer_tons is a list representing the tons of each fertilizer,
                    in the form [F1, F2, F3, F4].
    unit_prices is a list representing the price of one unit of each grain,
                in the form [oat_price, wheat_price, corn_price, barley_price, soy_price].
    The return value is a list in the form [oat_units, wheat_units, corn_units, barley_units, soy_units]
    """
    units_to_produce = [0, 0, 0, 0, 0]

    # Append amount for each grains
    for idx, amount in enumerate(fertilizer_tons):
        SIMPLEX_TABLE[idx].append(amount)
    SIMPLEX_TABLE[-1].append(0)

    # Insert price for each grains
    for idx, price in enumerate(unit_prices):
        SIMPLEX_TABLE[-1][idx] = price * (-1)

    # Until the last row doesn't have any negative elements
    while (isIncludedNegative(SIMPLEX_TABLE[-1])):
        p_row, p_col = get_pivot(SIMPLEX_TABLE)
        value_optimize(SIMPLEX_TABLE, p_row, p_col)

    for row in SIMPLEX_TABLE:
        for idx, elem in enumerate(row):
            if idx <= 4 and not SIMPLEX_TABLE[-1][idx] and elem:
                units_to_produce[idx] = row[-1]
    return units_to_produce


def get_pivot(simplex_table):
    pivot_col = simplex_table[-1].index(min(simplex_table[-1]))
    pivot_row = -1
    pivot_elem = sys.maxsize

    for idx, row in enumerate(simplex_table):
        if idx == len(simplex_table)-1:
            break
        temp = row[-1] / row[pivot_col] if row[pivot_col] > 0 else sys.maxsize
        if temp < pivot_elem:
            pivot_row = idx
            pivot_elem = temp
    return pivot_row, pivot_col


def value_optimize(simplex_table, p_row, p_col):
    operand = 1 / simplex_table[p_row][p_col]
    simplex_table[p_row][p_col] *= operand
    for idx, elem in enumerate(simplex_table[p_row]):
        if idx == p_col:
            continue
        simplex_table[p_row][idx] *= operand

    for row_idx, row in enumerate(simplex_table):
        if row_idx == p_row or row[p_col] == 0:
            continue
        temp = row[p_col]
        for elem_idx, elem in enumerate(row):
            simplex_table[row_idx][elem_idx] -= (simplex_table[p_row][elem_idx] * temp)
