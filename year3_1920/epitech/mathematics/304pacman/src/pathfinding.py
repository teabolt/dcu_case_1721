#!/usr/bin/env python3

from queue import SimpleQueue
from utils import indicesOf, outError


def paths(board):
    """
    Return the paths for a board.
    board - a list of strings
            each string has the format:
            F = source
            P = goal
            w = no connection
            0 = connection

    Returns: board (in place) -
                a modified version of board
                with distances of the path taken, instead of empty squares.
    """
    source = getGhost(board)
    getPacman(board)  # we only do this for validation (goal will be hard-coded in dijkstra)
    boardDijkstra(board, source)
    return board


def getGhost(board):
    """Return the position of the ghost, or raise an error."""
    source = indicesOf(board, "F")
    if not source:
        outError("Can not find a ghost on the map.")
    elif len(source) != 1:
        outError("Multiple ghosts found.")
    else:
        return source[0]


def getPacman(board):
    """Return the position of the pacman, or raise an error."""
    goal = indicesOf(board, "P")
    if not goal:
        outError("Can not find a pacman on the map.")
    elif len(goal) != 1:
        outError("Multiple pacmans found.")
    else:
        return goal[0]


def boardDijkstra(board, source):
    """
    Apply dijkstra path finding to board, starting from source.
    Board is modified with the path taken.
    Returns True if the goal was found, and False otherwise.
    """
    toVisit = SimpleQueue()

    distance = 1
    awayByOne = []
    for vertex in getNeighbours(board, source):
        i, j = vertex
        value = board[i][j]
        if value == 'P':
            return True
        else:
            board[i][j] = str(distance)
            awayByOne.append((i, j))
    toVisit.put(awayByOne)

    while not toVisit.empty():
        vertexList = toVisit.get()
        distance = (distance + 1)
        awayByN = []
        for visiting in vertexList:
            for vertex in getNeighbours(board, visiting):
                i, j = vertex
                value = board[i][j]

                if value == "P":
                    return True
                else:
                    board[i][j] = str(distance)
                    awayByN.append((i, j))
        if awayByN:
            toVisit.put(awayByN)
    return False


def getNeighbours(board, vertex):
    """
    Yield vertices (index tuples) that are neighbours of vertex
    and are a valid empty square (not visited before) in the board.
    The order of visiting is North, East, South, West.
    """
    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        i = vertex[0] + x
        j = vertex[1] + y
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            value = board[i][j]
            if value == "0" or value == "P":
                # in unvisited vertices and an empty cell
                yield (i, j)
