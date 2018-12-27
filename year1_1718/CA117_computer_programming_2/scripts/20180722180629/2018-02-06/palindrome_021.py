import sys

def palindrome(s):
    s_canon = ""
    for c in s.casefold():
        if c.isalnum():
            s_canon += c
    return s_canon == s_canon[::-1]

def main():
    for line in sys.stdin:
        print(palindrome(line.rstrip()))

if __name__ == "__main__":
    main()