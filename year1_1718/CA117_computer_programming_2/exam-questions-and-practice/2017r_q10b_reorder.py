#!/usr/bin/env python3

import sys
from r2017_q10a_queue import Queue
import copy

def reorder(q):
    q_copy = copy.deepcopy(q)
    new_q = Queue()
    tmp_q = Queue()

    while not q_copy.is_empty():
        e = q_copy.dequeue()
        if e % 2 == 0:
            new_q.enqueue(e)
        else:
            tmp_q.enqueue(e)

    while not tmp_q.is_empty():
        e = tmp_q.dequeue()
        new_q.enqueue(e)

    return new_q

def main():
    qu = Queue()
    for n in sys.stdin:
        qu.enqueue(int(n))
    print(reorder(qu).a)
    print(qu.a)

if __name__ == '__main__':
    main()