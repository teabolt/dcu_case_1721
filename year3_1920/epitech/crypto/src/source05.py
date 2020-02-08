#!/usr/bin/env python3

import sys
from repeating_xor_encryption import repeat_key, encrypt, decrypt
from hex_to_base64 import hex_to_unicode


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
            key = f.readline()
            if key == '':
                sys.exit(84)
            key = key.strip()
            plaintext = f.readline()
            if plaintext == '':
                sys.exit(84)
            plaintext = plaintext.strip()
    except:
        sys.exit(84)

    ciphertext = encrypt(plaintext, key)
    print(ciphertext)

    # print(hex_to_unicode(plaintext))
    # print(hex_to_unicode(decrypt(ciphertext, full_key)))


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)