#!/usr/bin/env python3

"""Entrance point to the 308reedpipes project."""

import sys
import os
import logging
from utils import (
    get_help,
    error_exit,
    parse_args,
    print_vec,
    print_interpolation,
)
from spline import (
    interpolate
)

if os.getenv('DEBUG', 'FALSE') == 'TRUE':
    logging.root.setLevel(logging.NOTSET)  # will see logs in standard output

def main():
    argc = len(sys.argv)
    if argc == 2:
        if sys.argv[1] == '-h':
            print(get_help())
        else: 
            error_exit('Invalid arguments')
    elif argc == 7:
        r0, r5, r10, r15, r20, n = parse_args(sys.argv)
        logging.info('Parsed arguments - radii: {}, {}, {}, {}, {}, number of points: {}'.format(
            r0, r5, r10, r15, r20, n
        ))
        points = [(0, r0), (5, r5), (10, r10), (15, r15), (20, r20)]
        vec, interpolation = interpolate(points, n)
        print_vec(vec)
        print_interpolation(interpolation)
    else:
        error_exit('In correct argument number (Expected 6). Got %d arguments' % (argc - 1))


if __name__ == "__main__":
    main()