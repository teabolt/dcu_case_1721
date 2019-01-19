#!/usr/bin/env python3

def maximum(lst):
    assert len(lst) > 0

    if len(lst) == 1:
        return lst[0]

    split = len(lst)//2
    return maxi(maximum(lst[:split]), maximum(lst[split:]))

def maxi(a, b):
   if a >= b:
      return a
   else:
      return b