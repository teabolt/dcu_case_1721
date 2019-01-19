#!/usr/bin/env python3

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        return self.head.item

    def add(self, item):
        self.head = Node(item, self.head)
        if self.tail == None:
            self.tail = self.head

    def addlast(self, item):
        # Add onto the tail
        if self.isempty():
            # If the queue is empty ...
            # Create a new node. Both head and tail will point to it.
            self.tail = Node(item, None)
            self.head = self.tail
        else:
            # Create a new node at the tail
            self.tail.next = Node(item, None)
            # But the tail should be moved on to the end of the list.
            self.tail = self.tail.next

    def remove(self):
        if self.isempty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            if self.head == None:
                self.tail = None
            return item

    def isempty(self):
        return self.head == None