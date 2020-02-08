#!/usr/bin/env python3

from board import Board2dArr as Board


class BrainMinimax(object):

    def __init__(self, board_size, max_minimax_depth=2):
        if board_size < 1:
            raise ValueError('Unsupported board size')
        self.board_size = board_size
        self.board = Board(board_size)
        self.max_minimax_depth = max_minimax_depth

    def update_state(self, p, x, y):
        # note that player p has made a move at coordinate x, y
        if p != 1 and p != 2:
            raise ValueError('p must be 1 or 2, got:', p)
        self.board.update(p, x, y)

    def make_move(self):
        # return coordinates at which this player wants to make a move
        if len(self.board) == 0:
            # empty board
            # pick a move by simple heuristics
            x, y = self.opening_move()
        else:
            # board has moves on it
            # use minimax algorithm
            x, y = self.find_best_move()
        self.update_state(1, x, y)
        # print(self.board)
        # print(self.board.board_cols)
        return x, y

    def undo_state(self, x, y):
        self.board.update(0, x, y)

    def find_best_move(self):
        # find the best move that should be made next
        best = max(((x, y) for (x, y) in self.next_moves()),
                    key=lambda move: self.simulate_move(move[0], move[1], self.minimax, 
                                                        True, 0, float('-inf'), float('inf')))
        return best

    def minimax(self, max_turn, curr_depth, alpha, beta):
        # use minimax algorithm to find best move
        # optimized with alpha-beta pruning
        if curr_depth == self.max_minimax_depth:
            # terminal state (base case)
            return self.evaluation_function()

        # recursive case
        if max_turn:
            # maximizer's turn
            opt = max  # optimization function
            guess = float('-inf')  # initial value for score
        else:
            # minimizer's turn
            opt = min
            guess = float('inf')

        best_score = guess  # initialize guess
        for x, y in self.next_moves():
            best_score = self.simulate_move(x, y, 
                                           lambda args: opt(args[0], self.minimax(*args[1:])),
                                           (best_score, False, curr_depth+1, alpha, beta))
            if max_turn:
                # choose which local pruning variable to update
                alpha = opt(best_score, alpha)
            else:
                beta = opt(best_score, beta)

            if beta <= alpha:
                # alpha-beta prune
                break

        return best_score

    def simulate_move(self, x, y, callback, *args):
        # do a move (as own player), call callback, undo move
        # return callback's value
        # use internal board state structure
        # do not copy for memory efficiency
        self.update_state(1, x, y)
        val = callback(*args)
        self.undo_state(x, y)
        return val

    def next_moves(self):
        # return a generator of possible next moves
        for (x, y) in self.board.next_moves_neighbour(-1):
            # print('check move: {},{}'.format(x, y), flush=True, end=', ')
            yield (x, y)
        # print('', flush=True)

    def opening_move(self):
        # return a move for an empty board
        return self.board.middle_move()

    def evaluation_function(self):
        # TODO idea: evaluation function for a single move (not the entire board???)
        return self.board.evaluate()
