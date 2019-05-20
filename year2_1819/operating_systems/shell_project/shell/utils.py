#!/usr/bin/env python3
# Done by Tomas Baltrunas, student number 17350793, Computer Applications Year 2. For CA216 2019 shell assignment.

"""Utility functions"""


def index_any(a, chars):
    for ch in chars:
        try:
            return a.index(ch)
        except ValueError:
            pass
    raise ValueError("None of '{}'' are in the list".format(chars))


def delist_singleton(a):
    """
    [a] -> a, 
    [a, b, ...] -> [a, b, ...] (unmodified)
    """
    if isinstance(a, list) and len(a) == 1:
        return a[0]
    else:
        return a


def slice_to_list(iterable, step):
    if 0 < len(iterable):
        return [iterable[i:i+step] for i in range(0, len(iterable), step)] 
    else:
        return [iterable] # need this to preserve empty strings


def strip_around(s):
    """
    _ = whitespace character
    '___a__' -> 'a' (some surrounding whitespace, stripped)
    '_' -> '_' (eg: newline on its own, no change)
    """
    return s.strip() if s != '\n' else s


def strip_around_lines(lines):
    return [strip_around(line) for line in lines.splitlines()]