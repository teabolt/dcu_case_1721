class Node:
    def __init__(self):
        self.item = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, item):
        oldtop = self.top
        self.top = Node()
        self.top.item = item
        self.top.next = oldtop

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        return item


class OldStack:
#
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]