import sys

def main():
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        classes = 0
        digit = False
        lowercase = False
        uppercase = False
        special = False
        
        for c in s:
            if c.isdigit() and not digit:
                digit = True
                classes += 1
            elif c.islower() and not lowercase:
                lowercase = True
                classes += 1
            elif c.isupper() and not uppercase:
                uppercase = True
                classes += 1
            elif not c.isalnum() and not special:
                special = True
                classes += 1

        print(classes)
        s = sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()