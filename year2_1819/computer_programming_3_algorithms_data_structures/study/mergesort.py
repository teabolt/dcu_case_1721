#!/usr/bin/env python3

def merge(lst, l1, h1, l2, h2):
    lst1 = lst[l1:h1+1]
    lst2 = lst[l2:h2+1]
    newindex = l1
    index1 = 0
    index2 = 0
    while newindex <= h2:
        if index1 == len(lst1):
            # Copy all of lst2 to lst
            lst[newindex] = lst2[index2]
            index2 += 1
        elif index2 == len(lst2):
            # Copy all of lst1 to lst
            lst[newindex] = lst1[index1]
            index1 += 1
        elif lst1[index1] <= lst2[index2]:
            lst[newindex] = lst1[index1]
            index1 += 1
        else:
            lst[newindex] = lst2[index2]
            index2 += 1
        newindex += 1


def r_mergesort(lst, l1, h1, l2, h2):
    if l1 == h1 and h2-l2 == 1:
        merge(lst, l1, h1, l2, h2)
        return None
    else:
        m1 = (l1+h1)//2
        m2 = (l2+h2)//2
        r_mergesort(lst, l1, m1, m1, h1)
        r_mergesort(lst, l2, m2, m2, h2)


def mergesort(lst):
    mid = (len(lst)-1)//2
    r_mergesort(lst, 0, mid, mid, len(lst))


def main():
    a = list(map(int, input().split()))
    mergesort(a)
    print(a)


if __name__ == '__main__':
    main()