import sys

def main():
    h1 = "POS"
    h2 = "CLUB"
    h3 = "P"
    h4 = "W"
    h5 = "D"
    h6 = "L"
    h7 = "GF"
    h8 = "GA"
    h9 = "GD"
    h10 = "PTS"

    lines = []

    longest_club = 0
    s = sys.stdin.readline().rstrip()
    while 0 < len(s):
        tokens = s.split()
        club_name = " ".join(tokens[1:-8])
        if longest_club < len(club_name):
            longest_club = len(club_name)
        lines.append(s)
        s = sys.stdin.readline().rstrip()

    print("{:3} {:{}} {:>2} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(h1, h2, longest_club, h3, h4, h5, h6, h7, h8, h9, h10))
    for line in lines:
        tokens = line.split()
        print("{:3} {:{}} {:>2} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(tokens[0], tokens[1:-8], longest_club, tokens[-8], tokens[-7], tokens[-6], tokens[-5], tokens[-4], tokens[-3], tokens[-2], tokens[-1]))

if __name__ == "__main__":
    main()