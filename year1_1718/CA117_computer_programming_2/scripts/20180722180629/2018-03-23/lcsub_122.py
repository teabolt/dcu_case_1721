#!/usr/bin/env python3

import sys

# if working in terms of indices (j, k)
#def len_from_indices(t):
#    return (t[1]-1)-t[0]+1

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()

    s3 = s2 # save original s2 to later find index of lcsub in it
    # (workaround)
    # set s1 to be the shortest of s1 and s2
    if len(s2) < len(s1):
        tmp = s1
        s1 = s2
        s2 = tmp
    assert len(s1) <= len(s2)

    # set of all common substrings
    # (don't care about discarded repeats. Longest str is unique)
    csubs = set()
    # iterate through each character of the smaller substring
    i = 0 
    while i < len(s1): # finer control with a while loop to possibly change how i works
        # get all indices where curr. s1 character occurrs in s2
        char_indices = []
        j = 0
        while j < len(s2):
            if s1[i] == s2[j]:
                char_indices.append(j)
            j += 1

        # get to all chars in s2 that are the curr. s1 char
        for ci in char_indices:
            # use linear search to find the first character that is not in both
            # strings, starting from an s2 char that is the curr. s1 char
            # 'parallel' comparison
            k = ci + 1 # end of s2 substring
            u = i + 1  # end of s1 substring
            while k < len(s2) and u < len(s1) and s2[k] == s1[u]:
                k += 1
                u += 1
            csubs.add(s2[ci:k]) # include the common substring
        i += 1

    # to improve: sub-strings of substrings are being added to the set now
    # find a way to exclude them (if possible)
    # idea: i value changes differently

    lcsub = max(csubs, key=len) # find the longest common substring
    i = s3.find(lcsub) # get index (unique)
    ln = len(lcsub)

    print(lcsub, ln, i)

if __name__ == '__main__':
    main()