#!/usr/bin/env python3

class Queue(object):

    def __init__(self):
        self.a = []

    def enqueue(self, e):
        self.a.append(e)

    def dequeue(self):
        return self.a.pop(0)

    def first(self):
        return self.a[0]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.a)

def main():
    q = Queue()
    print(len(q))
    q.enqueue(1)
    q.enqueue(2)
    print(q.first())
    print(q.is_empty())
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(len(q))
    try:
        print(q.dequeue())
    except IndexError:
        print('Error')
    try:
        print(q.first())
    except IndexError:
        print('Error')

if __name__ == '__main__':
    main()