#/usr/bin/env python

import func_bsearch

def count(a, q):
    # Returns the number of times 'q' occurs inside 'a'.
    count = 0
    p = func_bsearch.bsearch(a, q)
    if p < len(a) and a[p] == q: # Check if a[p] is q.
        not_q = func_bsearch.bsearch(a, q+1) # Find the first occurence of a value greater than q - first non-duplicate.
        number = not_q - p # Number of duplicates is the difference between the first duplicate and the first non-duplicate indices.
        return number
    else:
        return 0

assert count([1, 2, 3], 3) == 1
assert count([3, 4, 6], 5) == 0
assert count([2, 7, 7, 8, 9], 7) == 2