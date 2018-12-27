#!/usr/bin/env python

import func_bsearch

def contains(a, q):
    p = func_bsearch.bsearch(a, q)
    return p < len(a) and a[p] == q

# Tests

assert contains([1, 2, 3], 3)
assert not contains([2, 4, 6], 0) # 2nd bool. expression.
assert not contains([1, 3, 5], 6) # 1st bool. expression.
assert not contains([2, 4], 3) # 2nd bool. expression.

# More tests(not mine)

assert not contains([2,3,6,6,7,8], 1)
assert contains([2,3,6,6,7,8], 2)
assert contains([2,3,6,6,7,8], 6)
assert contains([2,3,6,6,7,8], 8)
assert not contains([2,3,6,6,7,8], 9)
assert not contains([2,3,6,6,7,8], 4)