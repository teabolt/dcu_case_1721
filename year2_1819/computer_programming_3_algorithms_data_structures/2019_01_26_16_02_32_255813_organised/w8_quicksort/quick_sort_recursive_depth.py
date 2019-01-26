
#
#   qsort code and a partition function.
#
#   Modify the qsort function so that it returns the maximum depth of recursion.
#
def partition(lst, lo, hi):
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        
    return hi

def rec_qsort(lst, lo, hi):
    rdepth = 0 # initial recursive depth - no recursive calls
    if lo < hi:
        rdepth += 1    # will recurse one time (picking the deepest branch out of the two recursive calls)
        pivot = partition(lst, lo, hi)
        rdepth_l = rec_qsort(lst, lo, pivot - 1) # depth of the left guy
        rdepth_r = rec_qsort(lst, pivot + 1, hi) # depth of the right guy
        rdepth += max(rdepth_l, rdepth_r) # the deeper of the branch recursion is added
        return rdepth
    else:
        return rdepth # did not recurse - my maximum is 0

def qsort(lst):
    return rec_qsort(lst, 0, len(lst) - 1)