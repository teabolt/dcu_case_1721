
# def insertion_sort(lst):
#     count_cmp = 0
#     count_swap = 0
#     # At each pass ensure that that section is sorted.
#     for todo in range(1, len(lst)):
#         # Find correct position for lst[todo].
#         i = todo
#         count_cmp += 1
#         while i > 0 and lst[i] < lst[i-1]:
#             count_swap += 1
#             lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
#             i -= 1
#             if i > 0:
#                 count_cmp += 1
#     return (count_cmp,count_swap)
    
    
def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    cmp_count = 0
    swp_count = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        loop_n = 0   # count the number of times the loop executes
        while i > 0 and lst[i] < lst[i-1]:
            loop_n += 1
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
        cmp_count += loop_n
        swp_count += loop_n
        if i > 0:    # check if early break
            cmp_count += 1
    return (cmp_count, swp_count)
