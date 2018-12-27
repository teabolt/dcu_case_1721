#!/usr/bin/env python3

import sys

def class_no(password):
        digit = 0
        lowercase = 0
        uppercase = 0
        special = 0
        
        for c in password:
            if c.isdigit():
                digit = 1
            elif c.islower():
                lowercase = 1
            elif c.isupper():
                uppercase = 1
            else:
                special = 1

        return digit + lowercase + uppercase + special

def main():
    for line in sys.stdin:
        print(class_no(line.rstrip()))

if __name__ == "__main__":
    main()