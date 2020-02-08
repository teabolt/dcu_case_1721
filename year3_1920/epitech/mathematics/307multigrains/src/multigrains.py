#!/usr/bin/env python3

"""Entrance point to the 307multigrains project."""

import sys
import os
from utils import (
    get_help,
    error_exit,
    parse_args,
    print_produce,
    total_sales,
)
from simplex import (
    optimize,
)

import logging
if os.getenv('DEBUG', 'FALSE') == 'TRUE':
    logging.root.setLevel(logging.NOTSET)  # will see logs in standard output


def main():
    argc = len(sys.argv)
    if argc == 2:
        if sys.argv[1] == '-h':
            print(get_help())
        else:
            error_exit('Argument not understood: "%s"' % sys.argv[1])
    elif argc == 10:
        n1, n2, n3, n4, po, pw, pc, pb, ps = parse_args(sys.argv)
        fertilizer_tons = [n1, n2, n3, n4]
        unit_prices = [po, pw, pc, pb, ps]
        logging.info('Parsed arguments: fertilizers: {}; units: {}'.format(fertilizer_tons, unit_prices))
        print('Resources: {} F1, {} F2, {} F3, {} F4'.format(*fertilizer_tons))
        print()
        units_to_produce = optimize(fertilizer_tons, unit_prices)
        logging.info('Units to produce: {}'.format(units_to_produce))
        print_produce(units_to_produce, unit_prices)
        print()
        sales = total_sales(units_to_produce, unit_prices)
        logging.info('Total sale amount: {}'.format(sales))
        print('Total production value: ${:.2f}'.format(sales))
    else:
        error_exit('Incorrect argument number (Expected 9). Got %d arguments' % (argc - 1))


if __name__ == '__main__':
    main()
