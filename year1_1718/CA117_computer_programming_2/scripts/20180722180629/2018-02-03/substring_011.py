import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        tokens = s.split()
        tokens[0] = tokens[0].lower()
        tokens[1] = tokens[1].lower()
        print(tokens[0] in tokens[1])
        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()