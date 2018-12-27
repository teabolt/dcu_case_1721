from stack_092 import Stack

lefties = '({['
righties = ')}]'

def matcher(line):
    s = Stack()
    for e in line:
        if e in lefties:
            s.push(e)
        if e in righties:
            s.pop()

    return False