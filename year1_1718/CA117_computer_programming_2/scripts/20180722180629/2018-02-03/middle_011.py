import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        mid = len(s) // 2
        if len(s) % 2 != 0:
            print(s[mid])
        else:
            print("No middle character!")
        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()