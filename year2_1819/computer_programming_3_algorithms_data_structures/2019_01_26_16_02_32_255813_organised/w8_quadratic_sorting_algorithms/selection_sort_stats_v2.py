
""" Selection sort algorithm """
def selection_sort(lst):
    cmp_count = 0
    mov_count = 0
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
            cmp_count += 1
        # place smallest at the beginning (swap min index with i)
        if min_index != i:  # no 'comparison' here (doesn't involve access to a list)
            lst[i], lst[min_index] = lst[min_index], lst[i]
            mov_count += 3  # indeed did a swap
    return (cmp_count, mov_count)

