
#
#   Insertion Sort
#
#   First place the smallest element at the front of the list to act as a sentinel
#
def insertion_sort(lst):
    cmp_count = 0
    mov_count = 0
    if len(lst) == 0:
        return (cmp_count, mov_count)

    # Find the smallest element
    min_index = 0   # assuming this is not a move (move outside loop - almost no effect)???
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i; # not a move as found out from upload
        cmp_count += 1 # just did a comparison (even if didn't enter if)

    # Move smallest to the front (swap elements min_index and 0)
    lst[0], lst[min_index] = lst[min_index], lst[0]
    mov_count += 3  # swap of two elements requires 3 moves

    # Now, with the smallest in the front, we don't need to check i in the inner loop
    
    # At each pass ensure that that section is sorted (start at 2, cos smallest already in position).
    for todo in range(2, len(lst)):
        # Find correct position for lst[todo]
        store = lst[todo]
        mov_count += 1 # save the current element
        i = todo    # (this is not a move according to previous questions???)
        while store < lst[i-1]: # Don't need to check i > 0
            cmp_count += 1 # just did a comparison
            lst[i] = lst[i-1] # Make space for the item
            mov_count += 1 # made a move when overriding / shifting
            i -= 1
        cmp_count += 1  # did a last comparison to get out of the loop
        lst[i] = store  # Found the place for this item, plonk it in
        mov_count += 1 # one final move

    return (cmp_count, mov_count)

    # MOVE = ACCCESS AND MODIFY A LIST VALUE
