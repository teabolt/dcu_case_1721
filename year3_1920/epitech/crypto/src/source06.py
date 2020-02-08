#!/usr/bin/env python3

import sys
from repeating_xor_encryption import brute_force, decrypt, hamming_distance
from hex_to_base64 import hex_to_unicode, unicode_to_hex


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
            ciphertext = f.read()
            if ciphertext == '':
                sys.exit(84)
            ciphertext = ciphertext.strip()
    except:
        sys.exit(84)
    # print(hamming_distance(unicode_to_hex("Hello"), unicode_to_hex("World")))

    key = brute_force(ciphertext)
    plaintext = decrypt(ciphertext, key)

    print(key)
    # print(plaintext)
    # print(hex_to_unicode(plaintext))


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)