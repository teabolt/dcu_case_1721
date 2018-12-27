import sys

def main():
    headers = ["POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"]
    data = []

    longest_club = 0
    for line in sys.stdin:
        tokens = line.rstrip().split()
        club = " ".join(tokens[1:-8])
        
        if longest_club < len(club):
            longest_club = len(club)

        data.append(tokens[:1] + [club] + tokens[-8:])

    format_s = "{:>3} {:{}} {:>2} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}"
    # for Python versions before 3.5, the unpacking operator * is usable only once in a function call
    print(format_s.format(headers[0], headers[1], longest_club, *headers[2:]))
    for row in data:
        print(format_s.format(row[0], row[1], longest_club, *row[2:]))

if __name__ == "__main__":
    main()
