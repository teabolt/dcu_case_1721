#!/usr/bin/env python3

import sys
from hex_to_base64 import hex_to_base64


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
            content = content.strip()  # remove newlines
    except:
        # TODO: replace pure except with specific exceptions to catch i.e. FileNotFoundException.
        sys.exit(84)

    base64 = hex_to_base64(content)
    print(base64)


if __name__ == '__main__':
    try:
        # big cheat
        main()
    except:
        sys.exit(84)


# TODO: replace the same try-except and sys.exit calls across all programs with something