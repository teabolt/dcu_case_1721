#!/usr/bin/env python3

import sys

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
    """Return the boggle points that a word with a length would score"""
    N = len(w)
    if N > 8: # upper bound
        N = 8
    return points_table[N]

def words(b, d):
    """Return a list with all the words that can be made from the dictionary d and boggle board b"""
    ws = []
    makew
    return ws

def main():
    with open(sys.argv[1], 'r') as boards_in: # boggle boards
        boards = [line.strip() for line in boards_in]
    with open(sys.argv[2], 'r') as dict_in: # dictionary of valid words
        d = [line.strip() for line in dict_in]
    
    for b in boards: # process each board
        words = words(b, d) # get all constructible words
        max_points = sum([get_points(w) for w in words])
        print('Possible points: {}'.format(max_points))

if __name__ == '__main__':
    main()