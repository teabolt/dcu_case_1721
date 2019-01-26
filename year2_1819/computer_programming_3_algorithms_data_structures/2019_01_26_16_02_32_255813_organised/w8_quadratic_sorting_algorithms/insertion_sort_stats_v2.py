
# def insertion_sort(lst):
#     count_cmp = 0
#     count_swap = 0
#     for todo in range(1, len(lst)):
#         tobeinserted = lst[todo]
#         i = todo
#         count_cmp += 1
#         while i > 0 and tobeinserted < lst[i-1]:
#             count_swap += 1
#             lst[i] = lst[i-1] # Make space for the item
#             i -= 1
#             if i > 0:
#                 count_cmp += 1
#         lst[i] = tobeinserted# Found the place for this item, plonk it in

#     return (count_cmp,count_swap)

def insertion_sort(lst):
    # No swap version
    cmp_count = 0
    mov_count = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        mov_count += 1 # remember the element
        i = todo
        while i > 0 and tobeinserted < lst[i-1]:
            cmp_count += 1  # just checked the condition and got inside the loop
            lst[i] = lst[i-1] # Make space for the item
            mov_count += 1 # did an override
            i -= 1
        if i > 0: # check if early break out of the loop
            cmp_count += 1  # did +1 compare to get out of the loop 
        # (no compare is done if 'i > 0' is false - 'and' is short-circuited)
        lst[i] = tobeinserted # Found the place for this item, plonk it in
        mov_count += 1  # move the element to the right place
    return (cmp_count, mov_count)
