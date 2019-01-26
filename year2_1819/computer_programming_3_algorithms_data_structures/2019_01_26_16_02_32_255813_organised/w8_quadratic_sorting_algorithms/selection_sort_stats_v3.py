
"""
    Selection sort algorithm

    This version of selection sort simultaneously gets the smallest and the largest
    and swaps them with the first and last element respectively.
    
    Timing tests show that it is about 7% faster on random input of size 10000
    
    Is it worth the extra effort?
    No. Use an NlogN algorithm instead for 1000* improvement.

"""
def selection_sort(lst):
    cmp_count = 0
    mov_count = 0
    lo = 0
    hi = len(lst) - 1
    while lo < hi:
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            if lst[j] < lst[min_index]:
                min_index = j
                cmp_count += 1  # did this compare (true), the rest will be skipped
            elif lst[j] > lst[max_index]: # maybe >= to get stable sort
                max_index = j
                cmp_count += 2  # did this compare (true) + the one before (false)
            else:   # own addition
                cmp_count += 2  # did two compares (both were false)

        if max_index == lo:
            max_index = min_index   # We will be moving lst[lo] to min_index, so update max_index first

        # swap min index with lo ... place smallest at the first
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        mov_count += 3  # swap for min
        # swap max index with hi ... place largest at the end
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        mov_count += 3  # swap for max
        lo += 1
        hi -= 1
    return (cmp_count, mov_count)
