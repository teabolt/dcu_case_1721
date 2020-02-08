#!/usr/bin/env python3

import sys


HELP_MESSAGE = """USAGE
./304pacman file c1 c2
\tfile\tfile describing the board, using the following characters:
\t\t‘0’ for an empty square,
\t\t‘1’ for a wall,
\t\t‘F’ for the ghost’s position,
\t\t‘P’ for Pacman’s position.
\tc1\tcharacter to display for a wall
\tc2\tcharacter to display for an empty space.\n"""



ALLOWED_MAP_SYMBOLS = {"0", "1", "F", "P"}


def readFile(fileName):
    """Read the map input at fileName into a data structure."""
    try:
        with open(fileName) as f:
            board = []
            for line in f:
                line = line.strip()
                validateLine(line)
                # replace walls with the symbol 'w'
                # this is to make things easier for the path finding function
                line = line.replace("1", "w")
                board.append([ch for ch in line])
                if len(board[0]) != len(line):
                    outError("File with different line sizes")
        return board
    except FileNotFoundError:
        outError("File not found")


def validateLine(line):
    """Check that the read line contains only the allowed symbols: 0, 1, F, P."""
    for ch in line:
        if ch not in ALLOWED_MAP_SYMBOLS:
            outError("Disallowed symbol found: '%s'" % ch)


def outError(message):
    """Write message to stderr and exit with error status."""
    sys.stderr.write(message + "\n")
    sys.exit(84)


def outBoard(board, wallChar, emptyChar):
    """Print the string representation of the board data structure"""
    for line in board:
        for char in line:
            if char == "w":
                print(wallChar, end="")
            elif char == "0":
                print(emptyChar, end="")
            elif char == "P" or char == "F":
                print(char, end='')
            else:
                number = int(char) % 10
                print(number, end="")
        print()


def outHelp():
    """Print a help message and exit with success status."""
    print(HELP_MESSAGE, end='')
    sys.exit(0)


def indicesOf(board, ch):
    """
    Find the indices of all matching characters in the board.
    Returns a list of 2-tuples.
    """
    indices = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ch:
                indices.append((i, j))
    return indices
