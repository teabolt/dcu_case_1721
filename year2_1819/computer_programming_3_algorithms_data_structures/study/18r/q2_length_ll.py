#!/usr/bin/env python3

from LinkedList import LinkedList


def testLength():
    ll = LinkedList()
    assert ll.length() == 0
    items = list(map(int, input().strip().split()))
    for item in items:
        ll.add(item)
    assert ll.length() == len(items)
    print(ll.length())
    ll.remove()
    assert ll.length() == len(items)-1
    while not ll.is_empty():
        ll.remove()
    assert ll.length() == 0


def main():
    testLength()


if __name__ == '__main__':
    main()