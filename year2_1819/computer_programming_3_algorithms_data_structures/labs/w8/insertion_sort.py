#!/usr/bin/env python3

import sys


def insertion_sort1(lst):
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
        if i > 0:    # check if early exit
            cmp_count += 1
    return (cmp_count, swp_count)


def insertion_sort2(lst):
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


def insertion_sort3(lst):
    cmp_count = 0
    mov_count = 0
    if len(lst) == 0:
        return (cmp_count, mov_count)

    # Find the smallest element
    min_index = 0   # assuming this is not a move (move outside loop - almost no effect)???
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i; 
            mov_count += 1 # set to new value
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



def main():
    # testISS1()
    # testISS2()
    testISS3()

def testISS3():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = insertion_sort3(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

    assert insertion_sort3([1, 2]) == (1, 3)


def testISS2():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = insertion_sort2(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

    assert insertion_sort2([letter for letter in 'abcdefghijklmnopqrstuvwxyz'])[1] == 50


def testISS1():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = insertion_sort1(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

    assert insertion_sort([1, 2]) == (1, 0)
    assert insertion_sort([2, 1]) == (1, 1)

if __name__ == "__main__":
    main()