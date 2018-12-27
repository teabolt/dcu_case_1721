import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        if 1 < len(s):
            print(s[0].capitalize() + s[1:-1] + s[-1].capitalize())
        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()