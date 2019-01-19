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

    def __str__(self):
        items = []
        ptr = self.head
        while ptr != None:
            items.append(str(ptr.item))
            ptr = ptr.next
        return ' '.join(items)


    def rotate(self):
        """First (at the head) element rotates to the left (goes to the end of the LinkedList)"""
        last = self.head
        while last != None and last.next != None:   # find the last node
            last = last.next
        if last != None and self.head.next != None:        # have at least two nodes
            last.next = Node(self.head.item, None)      # point the last node to the item at the head as the last node itself
            self.head = self.head.next                  # move up the head by one node
            # # alternative: first is last, comes to the head
            # self.head = Node(last.item, head.next)  # set the head to the item of the last node, still pointing to the second node
            # # pre_first is one node before the last node
            # pre_first = None    # destroy the last node

def testRotate():
    ll = LinkedList()
    items = list(map(int, input().split()))
    for item in items:
        ll.add(item)
    print(ll)
    ll.rotate()
    print(ll)


def detect_loop(ll):
    ptr = ll.head
    if ptr != None: # linky is not empty
        while ptr != None and ptr.next != ll.head:      # search for a circular node or stop at the end
            ptr = ptr.next
        if ptr != None:                                 # not at the end
            return True                                 # have a loop
        else:                                           # at the end
            return False
    else:   # empty linky
        return False



def add_loop(ll):
    if ll.head is not None:
        if ll.head.next is None:
            ll.head.next = ll.head
        else:
            ptr = ll.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = ll.head


def testLoop():
    ll_noloop = LinkedList()
    ll_loop = LinkedList()

    items = list(map(int, input().split()))

    print()
    for item in items:
        ll_noloop.add(item)
        ll_loop.add(item)
    print(detect_loop(ll_noloop))
    print(ll_noloop)
    print()
    print(ll_loop)
    add_loop(ll_loop)
    print(detect_loop(ll_loop))
    print(ll_loop)


def main():
    # testRotate()
    testLoop()


if __name__ == '__main__':
    main()