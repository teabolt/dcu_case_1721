#!/usr/bin/env python3

import sys


def get_groups(a, length):
    """Split iterable a into blocks of size length. Returns a generator."""
    return (a[i:i+length] for i in range(0, len(a), length))


def hex_xor(x, y):
    if len(x) != len(y):
        sys.exit(84)
    try:
        xor = int(x, base=16) ^ int(y, base=16)
        return format(xor, '0{}X'.format(len(x)))
    except:
        sys.exit(84)

    # OR ... manually
    # values = []
    # for a, b in zip(x, y):
        # xor = int(a, base=16) ^ int(b, base=16)
        # values.append(format(xor, 'X'))
    # return ''.join(values)


def byteslike_xor(a, b):
    return bytes([x^y for x, y in zip(a, b)])