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
        return self.enstack.is_empty() and self.destack.is_empty()

    def enqueue(self, item):
        self.enstack.push(item)

    def dequeue(self):
        if not self.destack.is_empty():
            return self.destack.pop()

        while not self.enstack.is_empty():
            self.destack.push(self.enstack.pop())
        return self.destack.pop()
        
    def __str__(self):
        return str(self.enstack) + ' - ' + str(self.destack)


def main():
    q = Queue()
    for letter in "abcd":
        q.enqueue(letter)
        print('stacks:', q)

    x = q.dequeue()
    print('stacks:', q)
    q.enqueue(x)
    print('stacks:', q)


    for letter in "ef":
        q.enqueue(letter)
        print('stacks:', q)

    while not q.isempty():
        print(q.dequeue())
        print('stacks:', q)


if __name__ == '__main__':
    main()