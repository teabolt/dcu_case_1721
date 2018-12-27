#!/usr/bin/env python3

import sys
#import time

def get_substrings(s):
    """Return a set of all the substrings of s. The empty string is excluded."""
    ss = set()
    for i in range(0, len(s)+1):
        j = i + 1
        while i < j < len(s)+1:
            ss.add(s[i:j])
            j += 1
    return ss

def main():
    #t1 = time.time()
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    
    ss1 = get_substrings(s1)
    ss2 = get_substrings(s2)
    ss_common = ss1 & ss2
    longest = max(ss_common, key=len)
    index = s2.index(longest)
    length = len(longest)

    print(longest, length, index)

    #t2 = time.time()
    #print(t2-t1)

if __name__ == '__main__':
    main()