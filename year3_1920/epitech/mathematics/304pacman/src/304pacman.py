#!/usr/bin/env python3

import sys
sys.path.append("src/")

import utils as u
import pathfinding as p


def main():
    argc = len(sys.argv)
    if argc != 4:
        if argc == 2 and sys.argv[1] == "-h":
            u.outHelp()
        u.outError("Error: Need more arguments")
    else:
        fileName, wallChar, emptyChar = sys.argv[1:]
        board = u.readFile(fileName)
        if len(board) == 0:
            u.outError("Empty File")
        p.paths(board)
        u.outBoard(board, wallChar, emptyChar)


if __name__ == "__main__":
    main()
