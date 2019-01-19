#!/usr/bin/env python3


#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
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
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += " " + ptr.item
            ptr = ptr.next
            
        return tmp_str


class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.add(item)

    def pop(self):
        return self.ll.remove()

    def is_empty(self):
        return self.ll.is_empty()


def main():
    stack = LinkedStack()
    
    tests = []
    
    tests.append(stack.is_empty())  # check the stack is empty first.
    tests.append(stack.pop() == None)
    
    val = 9
    stack.push(val)
    tests.append(not stack.is_empty())
    tests.append(stack.pop() == val)

    vowels = "aeiou"
    for c in vowels:
        stack.push(c)

    contents = ""
    while not stack.is_empty():
        contents += stack.pop()
        
    tests.append(vowels == contents[::-1])
    
    if all(tests):
        print("OK")
    else:
        print("Failed tests: ", end = "")
        for i in range(len(tests)):
            if not tests[i]:
                print(i, end = " " )
        print()

if __name__ == "__main__":
    main()