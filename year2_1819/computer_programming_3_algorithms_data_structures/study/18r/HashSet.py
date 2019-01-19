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


def main():
    size = int(input())
    items = list(map(int, input().split()))
    hs = HashSet(capacity=size)
    for item in items:
        hs.add(item)
    print(hs.average_bucket_length())


if __name__ == '__main__':
    main()