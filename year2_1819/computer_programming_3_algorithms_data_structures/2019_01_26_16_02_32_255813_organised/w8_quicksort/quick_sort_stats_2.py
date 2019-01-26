
#!/usr/bin/env python3

#
#   qsort code and a partition function.
#
#   Modify the partition function so that it uses the middle element.
#
def partition(lst, lo, hi):
    cmps, movs = 0, 0

    # pick the middle element as the pivot
    # (where there is an even number of elements, pick the 'left middle' element)
    mid = (lo+hi) // 2
    # swap middle into low/first
    # why, I don't know
    lst[mid], lst[lo] = lst[lo], lst[mid]
    movs += 3
    
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            cmps += 1
            lo += 1
        cmps += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            cmps += 1
            hi -= 1
        cmps += 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            movs += 3

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        movs += 3
    cmps += 1
    
    return (hi, cmps, movs)

def rec_qsort(lst, lo, hi):
    cmps, movs = 0, 0
    if lo < hi:
        pivot, cmps_p, movs_p = partition(lst, lo, hi)  # stats for the partition
        cmps_l, movs_l = rec_qsort(lst, lo, pivot - 1)  # stars for left recursion
        cmps_r, movs_r = rec_qsort(lst, pivot + 1, hi)  # stars for right recursion
        cmps += cmps_p + cmps_l + cmps_r
        movs += movs_p + movs_l + movs_r
    return (cmps, movs)

def qsort(lst):
    return rec_qsort(lst, 0, len(lst) - 1)


def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    # items = [int(item) for item in items]
    
    # print(items)
    # print('Partition :', partition(items, 0, len(items)-1), items)

    orig = list(items)
    result = qsort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)


if __name__ == '__main__':
	main()