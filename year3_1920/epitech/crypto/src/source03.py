#!/usr/bin/env python3

import sys
from byte_xor_encryption import (
    brute_force,
)


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
            content = f.read()
            if content == '':
                sys.exit(84)
    except:
        sys.exit(84)

    ciphertext = content.strip()
    key = brute_force(ciphertext)
    print(key)


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)