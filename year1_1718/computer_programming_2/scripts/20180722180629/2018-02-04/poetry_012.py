import sys

def main():
    lines = []
    longest = 0

    s = sys.stdin.readline()
    while 0 < len(s):
        lines.append(s)
        if longest < len(s):
            longest = len(s)
        s = sys.stdin.readline()

    for line in lines:
        print("{:^{}}".format(line.rstrip(), longest))

if __name__ == "__main__":
    main()