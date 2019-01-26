
""" Selection sort algorithm """
def selection_sort(lst):
    cmp_count = 0
    mov_count = 0
    for i in range(len(lst) - 1):   # go from 0 to one less the last index
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):    # go from one more than the start of the sublist to the end
            if lst[j] < lst[min_index]:
                min_index = j
            cmp_count += 1  # did a compare in the if condition (regardless if entered/didn't the if body)
        # place smallest at the beginning (swap min index with i)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        mov_count += 3  # a swap is three moves (tmp=lst[i], lst[i]=lst[min_index], lst[min_index]=tmp)
        # a move involves an access of a list in an assignment statement
    return (cmp_count, mov_count)

