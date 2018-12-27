import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        if 2 < len(s):
            print(s[1:-1])
        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()