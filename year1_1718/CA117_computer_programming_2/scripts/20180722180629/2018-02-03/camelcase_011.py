import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        words = s.split()

        i = 0
        while i < len(words):
            words[i] = words[i].capitalize()
            i += 1
        
        print(" ".join(words))
        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()