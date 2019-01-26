
#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

#
#   LinkedList class
#
class LinkedList:
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

    def count_even(self):
    	return self.ecount(self.head)

    def ecount(self,ptr):
    	if ptr == None:
    		return 0
    	elif ptr.item % 2 == 0:
    		return self.ecount(ptr.next) + 1
    	else:
    		return self.ecount(ptr.next)