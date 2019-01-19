#!/usr/bin/env python3

import sys
import random

def maximum(lst):
    assert len(lst) > 0

    # base case (singleton)
    if len(lst) == 1:
        return lst[0]

    # recursive case (split the lists up, return the larger list)
    split = len(lst)//2
    return maxi(maximum(lst[:split]), maximum(lst[split:]))


# charles daly
def maxi(a, b):
   if a >= b:
      return a
   else:
      return b


def main():
    args = sys.argv[1:]
    a = [int(arg) for arg in args]
    print(maximum(a))
    for i in range(100):
        rand = [random.randint(-100, 100) for n in range(100)]
        max_native = max(rand)
        max_implem = maximum(rand)
        if max_native != max_implem:
            print(i)
            print(rand, max_native, max_implem)


if __name__ == "__main__":
   main()