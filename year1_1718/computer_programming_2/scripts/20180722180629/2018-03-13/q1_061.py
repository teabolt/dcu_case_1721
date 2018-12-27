#!/usr/bin/env python3

import sys

def main():
    s, N = sys.argv[1:]
    N = int(N) % len(s)    
    sac = s[N:] + s[:N]
    print(sac)

if __name__ == '__main__':
    main()