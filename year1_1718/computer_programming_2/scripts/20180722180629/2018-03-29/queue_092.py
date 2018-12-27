#!/usr/bin/env python3

class Queue(object):
    # Model the queue ADT with a list wrapper

    def __init__(self):
        self.l = []

    def __len__(self):
        return len(self.l)

    def enqueue(self, e):
        self.l.append(e)

    def dequeue(self):
        return self.l.pop(0)

    def first(self):
        return self.l[0]

    def is_empty(self):
        return len(self.l) == 0