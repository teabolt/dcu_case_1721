import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        tokens = s.split()
        tokens[0] = tokens[0].lower()
        tokens[1] = tokens[1].lower()

        i = 0
        while i < len(tokens[0]) and (tokens[0][i] in tokens[1]):
            tokens[1] = tokens[1].replace(tokens[0][i], "", 1)
            i += 1

        if i == len(tokens[0]):
            print(True)
        else:
            print(False)

        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()