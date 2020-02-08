#!/usr/bin/env python3

import sys
from byte_xor_encryption import (
    decrypt,
    brute_force,
    find_message_score,
)
from hex_to_base64 import hex_to_unicode


# Problem:
# Each hex string when converted to unicode gives nonsense / nonprintable characters.
# I will thus brute force each string
# The string with the most sensible plaintext message
# will be assumed to be the string that was encrypted


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
            lines = f.readlines()
            if len(lines) == 0:
                sys.exit(84)
            ciphertexts = [line.strip() for line in lines]
    except:
        sys.exit(84)

    # brute force every example
    keys = [brute_force(text) for text in ciphertexts]
    # find the most english-like message
    top = sorted(enumerate(zip(ciphertexts, keys)), reverse=True, key=lambda item: find_message_score(item[1][0], item[1][1]))[0]

    # print line number and the key used for decryption
    line = top[0] + 1
    key = top[1][1]
    print(line, key)

    # for i, text in enumerate(ciphertexts):
    #     print(find_message_score(text))
        # print(text)
        # raw_message = hex_to_unicode(text)
        # print(raw_message)
        # print(get_score(raw_message))
        # print('with key')
        # key = brute_force(text)
        # print(key)
        # key_message = hex_to_unicode(decrypt(text, key))
        # print(key_message)
        # print(get_score(key_message))
        # print('---')


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)