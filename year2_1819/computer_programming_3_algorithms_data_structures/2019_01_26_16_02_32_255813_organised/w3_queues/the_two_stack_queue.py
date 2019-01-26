
#
#  Create a queue relying on a Stack. Actually Two Stacks.
#
#  The Stack ADT has three methods:
#     isempty(), push() and pop()
#
from Stack import Stack

class Queue:
    def __init__(self):
        """Initialise the queue"""
        self.enstack = Stack()
        self.destack = Stack()

    def isempty(self):
        return self.enstack.isempty() and self.destack.isempty()

    def enqueue(self, item):
        self.enstack.push(item)

    def dequeue(self):
        while not self.enstack.isempty():
        	self.destack.push(self.enstack.pop())
        	
        item = self.destack.pop()
        while not self.destack.isempty():
            self.enstack.push(self.destack.pop())
        
        return item