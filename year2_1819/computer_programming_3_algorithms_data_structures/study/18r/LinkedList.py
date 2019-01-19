#!/usr/bin/env python3

class Node(object):

    def __init__(self, item, pointer):
        self.item = item
        self.next = pointer


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def __len__(self):
        return self.length()

    def length(self):
        ptr = self.head
        total = 0
        while ptr != None:
            total += 1
            ptr = ptr.next
        return total

    def after(self, item):
        ptr = self.head
        while ptr != None and ptr.item != item:
            ptr = ptr.next
        return ptr.next.item if (ptr != None and ptr.next != None) else None

    def __in__(self, item):
        return self.contains()

    def contains(self, item):
        ptr = self.head
        while ptr != None and ptr.item != item:
            ptr = ptr.next
        return ptr != None

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next