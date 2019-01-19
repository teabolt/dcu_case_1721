#!/usr/bin/env python3

import LinkedList

class Queue:
    """ A linked list based queue """
    def __init__(self):
        self.length = 0
        self.linkedlist = LinkedList.LinkedList()

    def enqueue(self, item):
        self.linkedlist.addlast(item)
        self.length += 1

    def dequeue(self):
        if self.linkedlist.isempty():
            return None
        else:
            self.length -= 1
            return self.linkedlist.remove()

    # Examine the front of the queue without removing anything.
    def first(self):
        return self.linkedlist.peek()

    def isempty(self):
        return self.linkedlist.isempty()

    def __len__(self):
        return self.length