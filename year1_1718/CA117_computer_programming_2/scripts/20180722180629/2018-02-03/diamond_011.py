import sys

def main():
    n = int(sys.argv[1])
    max_line = 2*n - 1

    for line in range(1, max_line+1):
        spaces = abs(n - line)
        asters = n - spaces

        print(" "*spaces + "*", end='')
        asters = asters - 1
        print(" *"*asters)

if __name__ == "__main__":
    main()