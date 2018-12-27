import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        tokens = s.split()
        digits = tokens[0]
        base = int(tokens[1])
        total = 0

        i = 0
        while i < len(digits):
            total += int(digits[len(digits)-i-1])*base**i
            i += 1

        print(total)

        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()