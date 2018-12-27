#!/usr/bin/env python3

import sys
from priority_queue_112 import PQ

def main():
    # an implementation that doesn't load all the integers into memory
    # it's assumed that at least M+1 elements can be held in memory at a time

    M = int(sys.argv[1]) # number of minimum elements required
    pq = PQ() # data structure to use

    # initially read M elements
    for i in range(M):
        n = int(sys.stdin.readline())
        pq.insert(n)

    # read and delete +1 element until N is exhausted
    for n in sys.stdin:
        pq.insert(int(n)) # pq size will be M+1
        pq.delMax() # return to size M

    assert(pq.size() == M) # pq has M elements left, which are the M smallest integers

    while not pq.is_empty():
        print(pq.delMax()) # output all in descending order

if __name__ == '__main__':
    main()