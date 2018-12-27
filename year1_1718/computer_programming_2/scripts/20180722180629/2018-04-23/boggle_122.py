#!/usr/bin/env python3

import sys

# board index (zero-based, to later easily access the values) -> 
# neighbours of that index (tuple - neigbours won't change and iteration is fast)
neighbours = {
    0: (1, 4, 5),
    1: (0, 2, 4, 5, 6),
    2: (1, 3, 5, 6, 7),
    3: (2, 6, 7),
    4: (0, 1, 5, 8, 9),
    5: (0, 1, 2, 4, 6, 8, 9, 10),
    6: (1, 2, 3, 5, 7, 9, 10, 11),
    7: (2, 3, 6, 10, 11),
    8: (4, 5, 9, 12, 13),
    9: (4, 5, 6, 8, 10, 12, 13, 14),
    10: (5, 6, 7, 9, 11, 13, 14, 15),
    11: (6, 7, 10, 14, 15),
    12: (8, 9, 13),
    13: (8, 9, 10, 12, 14),
    14: (9, 10, 11, 13, 15),
    15: (10, 11, 14),
}
# hard-code or generate with a function (try...except IndexError)
# neighbours of i are i+1, i-1; i+4, i+4+1, i+4-1, i-4, i-4+1, i-4-1

points_table = {
    1:0,
    2:0,
    3:1,
    4:1,
    5:2,
    6:3,
    7:5,
    8:11,
}

def points(w):
    """Return the boggle points that a word, with its length, would score"""
    N = len(w)
    if N > 8: # upper bound
        N = 8
    return points_table[N]

def bsearch(a, q):
    """Binary search for query q in sorted list a"""
    low = 0
    high = len(a)

    while low < high:
        mid = (low+high)//2
        assert low <= mid < high

        if a[mid] < q:
            low = mid + 1
            assert a[low-1] < q
        else:
            high = mid
            assert q <= a[high]

    return low

def contains(a, q, p):
    """Return if query with value q is at position p in list a"""
    return p < len(a) and a[p] == q

def prefix(a, q, p):
    """Return if at list a, position p, query q is a prefix of the element that resides in that position"""
    return p < len(a) and a[p][:len(q)] == q # OR use s.startswith()

class Stack(object):
    """Model the stack ADT with a list wrapper
    Extra method 'contains', stripped of unused helper methods"""

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def contains(self, e):
        """Check if an element is not already on the stack"""
        l = set(self.l) # (duplicates don't matter)
        return e in l # a set's 'in' is fast

def make_words(b, d):
    """Return a list with all the words that can be made from the boggle board b and dictionary (of words) d"""
    words = [] # will be modified in-place by 'touch()'
    stack = Stack() # will use a stack to solve this problem

    # fill 'words' with valid words by 'tracing' the board in all kinds of ways
    trace(neighbours.keys(), b, d, stack, words) # start out with all the indices (keys)
    
    # exclude duplicates (same word - scores once) and words with length less than 3 (score no points)
    ws = set()
    for w in words:
        if 2 < len(w):
            ws.add(w)
    return ws

def trace(bindexes, bvalues, diction, stack, words):
    """Go through each element of 'bindexes'(*indices* of the board), using current word stack 'stack', 
    board *values* 'bvalues', list of valid words 'diction', and list 'words' where valid words should be added"""
    global neighbours # will reference this throughout

    # Essentially, iterate through each letter of the boggle board. Pick the first letter of the word (push it onto the stack).
    # Then add neighbouring letters, making sure you use each letter only once.
    # For each added letter, add their neighbours (again checking that you are not repeating), and so on (use recursion and looping).
    # As the program progresses, check (with fast binary search) that the word you form (in the stack) is in the list of valid words

    # To optimise, check if the word formed is at least a prefix in the list of valid words
    # Use a stack to add (push) letters and 'backtrack' (pop) in case they lead nowhere

    for i in bindexes: # go through each index
        # using indices instead of values because indices are unique and so can check that they don't repeat
        if stack.contains(i): # check if index is not in use
            continue # index is in use, so don't add

        stack.push(i) # add the index since it's not in use

        # make a word from the indices you've gotten so far
        # directly access the stack list or make a 'chained_value' method
        w = ''.join([bvalues[i] for i in stack.l])

        p = bsearch(diction, w) # find where the word fits
        
        if not prefix(diction, w, p): # check if the word is at least a prefix to the word that is in the position
            stack.pop() # if not, 'backtrack' by removing the last letter
            continue # try the next letter (if available)
        elif contains(diction, w, p): # check if you actually found a word
            words.append(w) # add the word to the makeable words list

        # recursive call
        # act on the neighbour indices
        # still reference the same stack
        trace(neighbours[i], bvalues, diction, stack, words)
        # exit condition is when the loop finishes (no more free neighbours to add)

        stack.pop() # finished, so remove the 'base' letter from which you were branching via neighbours and go onto the next one

def main():
    with open(sys.argv[1], 'r') as boards_in, open(sys.argv[2], 'r') as list_in: 
        boards = [line.strip() for line in boards_in] # boggle boards
        diction = [line.strip() for line in list_in]  # dictionary (list) of all the valid words
    
    for b in boards: # get points for each board
        possible_words = make_words(b, diction) # get all constructible words
        max_points = sum([points(w) for w in possible_words]) # get each word's points and sum up
        print('Possible points: {}'.format(max_points))

if __name__ == '__main__':
    main()