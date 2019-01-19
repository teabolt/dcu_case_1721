#!/usr/bin/env python3

from LinkedList import LinkedList


def testAfter():
    ll = LinkedList()
    find = int(input())
    items = list(map(int, input().strip().split()))
    print(find, items)
    print()
    assert ll.after(find) == None
    for item in items:
        ll.add(item)
    print(ll.after(find))
    while not ll.is_empty():
        ll.remove()
    assert ll.after(find) == None


def main():
    testAfter()


if __name__ == '__main__':
    main()