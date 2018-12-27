import sys

def count_tokens(s):
    return len(s.split())

def main():
    total = 0
    for line in sys.stdin:
        total += count_tokens(line.rstrip())
    print(total)

if __name__ == "__main__":
    main()