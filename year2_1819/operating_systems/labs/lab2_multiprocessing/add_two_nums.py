#!/usr/bin/env python3

import multiprocessing as mp


def addTwoNumbers(a, b, q):
    # time.sleep(5) # In case you want to slow things down to see what is happening.
    q.put(a+b)


def addTwoPar():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    q = mp.Queue()
    p1 = mp.Process(target=addTwoNumbers, args=(x, y, q))
    p2 = mp.Process(target=addTwoNumbers, args=(x, y, q))
    p1.start()
    p2.start()
    result1 = q.get()
    result2 = q.get()
    print(result1+result2)


def main():
    addTwoPar()


if __name__ == '__main__':
    main()