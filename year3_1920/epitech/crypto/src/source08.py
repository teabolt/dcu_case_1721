#!/usr/bin/env python3

import sys
import collections

from utils import get_groups
from hex_to_base64 import (
    base64_to_byteslike,
    base64_to_hex,
)


def get_score_ecb_encrypted(text):
    """Give a score for how likely that base64 encoded text is encrypted with ECB mode."""
    # The approach is as follows
    # In "hello there", ECB maps each "e" to the same byte in cyphertext.
    # if have English text, then certain bytes occur more frequently.
    text = base64_to_hex(text)
    characters = list(get_groups(text, 2))  # check each byte

    # we check the frequency of each byte
    frequencies = collections.Counter(characters)
    counts = frequencies.values()
    # get rid of what we counted only once
    # (otherwise each string has the same count)
    more_than_one = filter(lambda count: count != 1, counts)
    score = sum(more_than_one)
    return score
    # TODO: could also measure distance between each symbol?


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
            ciphertexts = f.readlines()
            if len(ciphertexts) == 0:
                sys.exit(84)
            ciphertexts = [text.strip() for text in ciphertexts]
    except:
        sys.exit(84)

    ecb_likelihood = sorted(enumerate(ciphertexts), reverse=True, key=lambda entry: get_score_ecb_encrypted(entry[1]))

    top = ecb_likelihood[0]
    line = top[0] + 1
    print(line)


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)