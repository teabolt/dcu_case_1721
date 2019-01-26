
#
#   qsort code and a partition function.
#
#   Modify the code so that it returns the number of compares and the number of moves.
#

def partition(lst, lo, hi):
    cmps = 0
    movs = 0
    part = lo # pick the first element to be the pivot
    # print('Part: ', part, lst[part])
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi: # search for first position from the left that has a value larger than the pivot's
            lo += 1
            cmps += 1
        # print('Low', lo, lst[lo])
        cmps += 1 # made a comparison to get out of the loop (whether the lo value is greater than the pivot's or lo becomes greater or hi)
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1                # search for the first position from the right that has a value smaller or equal to the pivot's
            cmps += 1
        # print('Hi', hi, lst[hi]) 
        cmps += 1 # made a comparison to get out of the loop (not using a sentinel to terminate)

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi] # correctly put the values to the left or to the right of the 'final'/'assumed' position of the pivot
            # print('Intermediate list: ', lst)
            movs += 3 # each two element swap is three moves

        # eg 1 iteration: lst[part] = 6
        # hi:                    |   |   |  |
        #       [6, 1, 4, 6, 7, -10, 8, 9, 10] -> [6, 1, 4, 6, -10, 7, 8, 9, 10]
        # lo:    |  |  |  |  |

        # continue on like this with values of lo and hi kept from the last iteration
    # finished
    # Swap part into position
    # lst[hi] will have a smaller value than lst[part] (result of linear search above)
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        movs += 3
    cmps += 1 # made a comparison regardless if the if ran or not
    return (hi, cmps, movs)

def rec_qsort(lst, lo, hi):
    cmps = 0
    movs = 0
    if lo < hi:
        pivot, p_cmps, p_movs = partition(lst, lo, hi)
        l_cmps, l_movs = rec_qsort(lst, lo, pivot - 1)
        r_cmps, r_movs = rec_qsort(lst, pivot + 1, hi)
        # the number of moves/compares I had is 
        # 1) my moves and compares when finding a partition +
        # 2) the moves and compares of the sublists partitioned
        cmps += p_cmps + l_cmps + r_cmps
        movs += p_movs + l_movs + r_movs
    return (cmps, movs)

def qsort(lst):
    cmps, movs = rec_qsort(lst, 0, len(lst) - 1)
    return (cmps, movs)