#!/usr/bin/env python3

from LinkedList import LinkedList


class HashSet(object):

    def __init__(self, capacity=10):
        self.table = [None] * capacity

    def add(self, item):
        h = hash(item)
        i = h % len(self.table)
        if self.table[i] == None:
            self.table[i] = LinkedList()

        if item not in self.table[i]:   # set
            self.table[i].add(item)

    def average_bucket_length(self):
        buckets = []
        for entry in self.table:
            if entry is not None:
                buckets.append(len(entry))
        return sum(buckets) / len(buckets) if buckets else None

    def min_max_bucket_length(self):
        i = 0
        while i < len(self.table) and self.table[i] is None:   # find first chain
            i += 1
        if i < len(self.table):             # if have a first chain
            maxb = len(self.table[i])       # initial guesses
            minb = len(self.table[i])
            for entry in self.table[i+1:]:  # start from first chain
                if entry is not None:
                    N = len(entry)
                    if maxb < N:          # update max
                        maxb = N
                    elif N < minb:        # update min
                        minb = N
            return (minb, maxb)
        else:                           # no chains, fall back
            return (0, 0)


def testAvg():
    size = int(input())
    items = list(map(int, input().split()))
    hs = HashSet(capacity=size)
    for item in items:
        hs.add(item)
    print(hs.average_bucket_length())


def testMinmax():
    size = int(input())
    items = list(map(int, input().split()))
    hs = HashSet(capacity=size)
    for item in items:
        hs.add(item)
    print(hs.min_max_bucket_length())


def main():
    testMinmax()


if __name__ == '__main__':
    main()