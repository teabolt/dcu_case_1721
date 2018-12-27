import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        vowels = ['a', 'e', 'i', 'o', 'u']

        if s[-2:] == "ch" or s[-2:] == "sh" or s[-1] == "x" or s[-1] == "s" or s[-1] == "z" or s[-1] == "o":
            print(s + "es")
        elif s[-2] not in vowels and s[-1] == "y":
            print(s[:-1] + "ies")
        elif s[-1] == "f":
            print(s[:-1] + "ves") 
        elif s[-2:] == "fe":
            print(s[:-2] + "ves")
        else:
            print(s + "s")

        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()