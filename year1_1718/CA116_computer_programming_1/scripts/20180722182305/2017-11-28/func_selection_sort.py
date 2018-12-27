#!/usr/bin/env python

def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j += 1
        tmp = a[i]
        a[i] = a[p]
        a[p] = tmp
        i += 1

def main():
    a = [4, 423, 1, 453, 23, 2, 3, 0, 19]
    print a
    selection_sort(a)
    print a
    a = [32, -32, 3, 2, 53]
    print a
    selection_sort(a)
    print a
    a = []
    print a
    selection_sort(a)
    print a
    a = [1]
    print a
    selection_sort(a)
    print a
    a = [-52.32, 43.32, 0.4, 0.4000001]
    print a
    selection_sort(a)
    print a
    a = ["ant", "apple", "rhino", "zebra", "bread"]
    print a
    selection_sort(a)
    print a

if __name__ == "__main__":
    main()