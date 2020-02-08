#!/usr/bin/env python3

import sys
from utils import hex_xor


def main():
    if len(sys.argv) != 2:
        print("""Usage:
              program filename

              filename - file whose contents will be transformed.
              """)
        sys.exit(84)
    file = sys.argv[1]
    try:
        with open(file) as f:
            hex_lines = f.readlines()
            if hex_lines == '':
                sys.exit(84)
            hex_lines = [line.strip() for line in hex_lines]
    except:
        sys.exit(84)

    xor = hex_xor(hex_lines[0], hex_lines[1])
    print(xor)


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)