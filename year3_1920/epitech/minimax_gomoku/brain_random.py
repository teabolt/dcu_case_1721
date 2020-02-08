#!/usr/bin/env python3

import random


class BrainRandom(object):

    def __init__(self, board_size):
        if board_size < 1:
            raise ValueError('Unsupported board size')
        self.board_size = board_size
        self.board_state = set()  # a simple set of (x, y tuples) for already placed stones

    def update_state(self, p, x, y):
        # note that player p has made a move at coordinate x, y
        # p = 0 - self
        # p = 1 - opponent
        self.board_state.add((x, y))

    def make_move(self):
        # return coordinates at which this player wants to make a move
        x, y = self.random_coordinates()
        while ((x, y)) in self.board_state:
            x, y = self.random_coordinates()
        self.update_state(0, x, y)
        return x, y

    def random_coordinates(self):
        x = random.randint(0, self.board_size-1)
        y = random.randint(0, self.board_size-1)
        return x, y
