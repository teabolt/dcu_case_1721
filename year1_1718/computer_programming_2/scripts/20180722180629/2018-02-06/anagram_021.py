import sys

def anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

def main():
    for line in sys.stdin:
        tokens = line.rstrip().split()
        print(anagrams(tokens[0], tokens[1]))

if __name__ == "__main__":
    main()