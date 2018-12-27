#!/usr/bin/env python3

import sys
from priority_queue_112 import PQ

def main():
    M = int(sys.argv[1]) # get command line argument
    pq = PQ()
    
    # admittedly, this loads all the numbers into memory
    for n in sys.stdin:
        pq.insert(int(n))

    # remove N-M numbers
    while pq.size() > M:
        pq.delMax()

    # return maximums(descending order) of the remaining M numbers
    assert(pq.size() == M)
    for i in range(M):
        print(pq.delMax())

if __name__ == '__main__':
    main()