#!/usr/bin/env python3

import re


class Board2dArr(object):
    # gomoku board representation as a 2D array

    # map from player to compiled regex object
    chain_regex = {
        # 1: re.compile(r'1{1,5}'),
        # 2: re.compile(r'2{1,5}'),
        1: re.compile(b'\x01{1,5}'),
        2: re.compile(b'\x02{1,5}'),
    }
    empty_value = 0
    p1_value = 1
    p2_value = 2
    num_players = 2

    def __init__(self, board_size):
        self.board_size = board_size
        # 2D bytearray
        # self.board = [[0]*board_size for _ in range(board_size)]
        self.board = [bytearray([self.empty_value]*board_size) for _ in range(board_size)]
        self.board_cols = [bytearray([self.empty_value]*board_size) for _ in range(board_size)]
        self.board_posdiag = self._generate_positive_diagonal()
        self.board_negdiag = self._generate_negative_diagonal()
        # update "chains" (stones in a row) dynamically as moves are made
        self.chains = ChainsContainer()

    def _generate_positive_diagonal(self):
        N = self.board_size
        posdiag = [[] for _ in range(N+N-1)]
        for i in range(N):
            for j in range(N):
                posdiag[i+j].append(0)
        return [bytearray(diag) for diag in posdiag]

    def _generate_negative_diagonal(self):
        N = self.board_size
        negdiag = [[] for _ in range(N+N-1)]
        for i in range(N):
            for j in range(N):
                negdiag[i-j-(-N+1)].append(0)
        return [bytearray(diag) for diag in negdiag]

    def __str__(self):
        # return matrix representation
        b = (''.join(str(x) for x in row) for row in self.board)
        return '\n'.join(b)

    def __len__(self):
        # return total number of moves made
        return sum(1 for (p, x, y) in self)

    def __iter__(self):
        # iterate through each move that was made
        for i in range(self.board_size):
            for j in range(self.board_size):
                p = self.get(i, j)
                if p != 0:
                    yield p, i, j

    def __contains__(self, coordinates):
        # true if coordinates x, y tuple is already a taken move
        x, y = coordinates
        p = self.get(x, y)
        return p != 0

    def in_bounds(self, x, y):
        # check that an x, y coordinates are inside the board
        # assuming zero-based indexing
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def is_empty(self, x, y):
        return self.board[x][y] == 0

    def get(self, x, y):
        # return the player OR empty square for coordinates x, y
        return self.board[x][y]

    def update(self, p, x, y):
        # p: 0 - empty cell, 1 - own player, 2 - other player
        self.board[x][y] = p
        self.board_cols[y][x] = p

        # FIXME
        posnum = self._posdiagonal_number(x, y)
        N = self.board_size - 1
        pos_offset = posnum-N if posnum > N else 0
        self.board_posdiag[posnum][y-pos_offset] = p

        negnum = self._negdiagonal_number(x, y, self.board_size)
        neg_offset = negnum-N if negnum > N else 0
        self.board_negdiag[negnum][y-neg_offset] = p

        # update chains state
        self._update_chains(x, y)

    def middle_move(self):
        mid = self.board_size // 2
        return (mid, mid)

    def random_move(self):
        raise NotImplementedError

    def next_moves_all_unoccupied(self):
        # return all positions that are unoccupied
        # this is very inefficient
        for i in range(self.board_size):
            for j in range(self.board_size):
                if (i, j) not in self:
                    # not in state
                    yield (i, j)

    def next_moves_proximity(self, p):
        # return moves with proximity p
        # next to already placed moves
        # moves next to each other have proximity (distance) 1
        # return filter(lambda move:
        #                 self.distance_to_nearest(move[0], move[1])[1] <= p, 
        #               self.next_moves_all_unoccupied())
        raise NotImplementedError

    # def distance_to_nearest(self, x, y):
    #     return min((((i, j), distance(x, y, i, j)) for i, j in self.state_values()),
    #                key=lambda item: item[1])

    def next_moves_neighbour(self, n):
        # return n next moves
        # if empty, seed middle
        # else near other squares
        moves = set()  # avoid overlapping neighbours by keeping tracking of moves already made
        for _, x, y in self:
            neighbours = list(filter(lambda move: not move in moves, 
                         filter(lambda move: not move in self, 
                         filter(lambda move: self.in_bounds(move[0], move[1]),
                         generate_matrix_neighbours(x, y)))))
            moves.update(neighbours)

            for i, j in neighbours:
                # print(i, j, flush=True)
                yield (i, j)
                n -= 1
                if n == 0:
                    break
            if n == 0:
                break
        # TODO: how to decide which moves to pick and which to discard?

    def evaluate(self):
        # evaluate the board's score
        # high value = maximizer is winning
        # low value = minimizer is winning
        self_points = self.evaluate_player(0)
        other_points = self.evaluate_player(1)
        score = self_points - other_points
        # print('points:', self_points, other_points)
        return score

    def evaluate_player(self, player):
        chains = list(self.chains.iter_all(player))
        scores = [self.evaluate_chain(chain) for chain in chains]
        if not scores:
            return 0
        else:
            return self.average(scores)

    @staticmethod
    def average(iterable):
        return sum(iterable)/len(iterable)

    @staticmethod
    def evaluate_chain(chain):
        # assign base score by hand
        points = 0
        if chain.length == 5:
            # winning move
            points = float('inf')
        elif chain.length == 4:
            points = 1000
        elif chain.length == 3:
            points = 100
        elif chain.length == 2:
            points = 10
        elif chain.length == 1:
            points = 1
        # linear combination
        # no endpoints kills the score
        # 2 endpoints doubles the score
        points *= chain.open_endpoints
        return points


    def _update_chains(self, x, y):
        # print(x, y)
        # print('before:', self.chains)
        # breakpoint()
        # delete chains at (x, y)

        self._update_chains_handler(x, y, 'horizontal',
                                    self._horizontal_number, self._row_lines)
        self._update_chains_handler(x, y, 'vertical',
                                    self. _vertical_number, self._column_lines)
        self._update_chains_handler(x, y, 'posdiagonal',
                                    self._posdiagonal_number, self._positive_diagonal_lines)
        self._update_chains_handler(x, y, 'negdiagonal',
                                    self._negdiagonal_number, self._negative_diagonal_lines, self.board_size)

        # print('after:', self.chains)

    def _update_chains_handler(self, x, y, direction, number_callback, line_callback, *args):
        num = number_callback(x, y, *args)
        self.chains.delete(direction=direction, number=num)

        line = line_callback(num=num)
        for player_idx in [0, 1]:
            # compute and add chains at (x, y)
            player_value = player_idx + 1
            matches = self._get_line_matches(player_value, line)
            chains = [Chain(match) for match in matches]
            self.chains.add(chains, player=player_idx, direction=direction, number=num)


    def _lines_at(self, x, y):
        lines = []
        lines += self._row_lines(y)
        lines += self._column_lines(x)
        lines += filter(self._long_diagonal, self._positive_diagonal_lines(x, y))
        lines += filter(self._long_diagonal, self._negative_diagonal_lines(x, y))
        return lines

    def _get_line_matches_all(self, line):
        matches = []
        matches += self._get_line_matches(self.p1_value, line)
        matches += self._get_line_matches(self.p2_value, line)
        return matches

    @classmethod
    def _get_line_matches(cls, player, line):
        return cls.chain_regex[player].finditer(line)

    @classmethod
    def _get_lines_matches(cls, player, lines):
        matches = []
        for line in lines:
            matches += cls._get_line_matches(player, line)
        return matches

    @staticmethod
    def _long_diagonal(diagonal):
        return len(diagonal) >= 5

    # (x, y) are coordinates in a top-to-bottom left-to-right coordinate space
    # they index a 2D array like [x][y]

    @staticmethod
    def _horizontal_number(x, y):
        return x

    @staticmethod
    def _vertical_number(x, y):
        return y

    @staticmethod
    def _posdiagonal_number(x, y):
        return x + y

    @staticmethod
    def _negdiagonal_number(x, y, N):
        # N is the length of the board
        return (y-x) + (N-1)  ### ??? FIXME is x and y same as i and j?


    @staticmethod
    def _get_row_lines(iterable, num=None):
        if num is None:
            return [row for row in iterable]
        else:
            return iterable[num]

    def _row_lines(self, num=None):
        return self._get_row_lines(self.board, num=num)

    @staticmethod
    def _get_col_lines(iterable, num=None):
        if num is None:
            return [list(col) for col in zip(*iterable)]
        else:
            N = len(iterable)
            return [iterable[j][i] for i in range(N) 
                                   for j in range(N)
                                   if i == num]

    def _column_lines(self, num=None):
        # return bytearray(self._get_col_lines(self.board, num=num))
        return self.board_cols[num]

    @staticmethod
    def _get_pos_diag_lines(iterable, num=None):
        # executed left to right, top to bottom
        if num is None:
            N = len(iterable)
            lines = [[] for _ in range(N+N-1)]
            for i in range(N):
                for j in range(N):
                    lines[i+j].append(iterable[i][j])
            return lines
        else:
            N = len(iterable)
            return [iterable[i][j] for i in range(N) for j in range(N) if i+j == num]

    def _positive_diagonal_lines(self, num=None):
        # based on https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        # /
        return self.board_posdiag[num]
        # if num is None:
        #     return [bytearray(diag) for diag in self._get_pos_diag_lines(self.board)]
        # else:
        #     return bytearray(self._get_pos_diag_lines(self.board, num=num))

    @staticmethod
    def _get_neg_diag_lines(iterable, num=None):
        # executed left to right, top to bottom
        if num is None:
            N = len(iterable)
            lines = [[] for _ in range(N+N-1)]
            for i in range(N):
                for j in range(N):
                    lines[i-j-(-N+1)].append(iterable[j][i])
            return lines
        else:
            N = len(iterable)
            return [iterable[i][j] for i in range(N) for j in range(N) if (j-i)+(N-1) == num]

    def _negative_diagonal_lines(self, num=None):
        # \
        return self.board_negdiag[num]
        # if num is None:
        #     return [bytearray(diag) for diag in self._get_neg_diag_lines(self.board)]
        # else:
        #     return bytearray(self._get_neg_diag_lines(self.board, num=num))


def generate_matrix_neighbours(x, y):
    for i in (-1, 0, +1):
        for j in (-1, 0, +1):
            yield (x+i, y+j)


def distance(x, y, i, j):
    # compute distance from (x, y) to (i, j)
    return max(abs(x-i), abs(y-j))


class ChainsContainer(object):
    # chains of a player
    # chains at certain coordinates and in a certain direction
    # check only rows/columns/diagonals for updated piece
    # for both players
    # return new chains or update old ones

    directions = {
        'horizontal': 0,
        'vertical': 1,
        'posdiagonal': 2,
        'negdiagonal': 3,
    }

    num_players = 2

    def __init__(self):
        # player -> direction -> chains (list)
        self.data = [[[] for _ in range(len(self.directions))] for _ in range(self.num_players)]
        # row num, col num, pdiag num, ndiag num

    def __str__(self):
        return str([[[[str(w) for w in z] for z in y] for y in x] for x in self.data])

    def iter_all(self, player=None):
        if player is not None:
            for dir_chains in self.data[player]:
                    for chain, num in dir_chains:
                        yield chain
        else:
            for p_chains in self.data:
                for dir_chains in p_chains:
                    for chain, num in dir_chains:
                        yield chain


    def add(self, chains, player=None, direction=None, number=None):
        for chain in chains:
            obj = (chain, number)
            slot = self.data[player][self.directions[direction]]
            slot.append(obj)

    def delete(self, player=None, direction=None, number=None):
        if player is not None and direction is not None and number is not None:
            # delete for a specific player
            slot = self.data[player][self.directions[direction]]
            items = self._find_by_number(slot, number)
            for item in items:
                slot.remove(item)
        if player is None and direction is not None and number is not None:
            # delete for all players
            for slot in self.data:
                slot = slot[self.directions[direction]]
                items = self._find_by_number(slot, number)
                for item in items:
                    slot.remove(item)

    @staticmethod
    def _find_by_number(slot, number):
        return filter(lambda x: x[1] == number, slot)


class Chain(object):
    """Represents stones/moves in a row."""

    def __init__(self, match):
        if not match:
            raise ValueError('Chain init match is empty')
        self.match = match
        self.length = self._get_length()
        self.open_endpoints = self._get_open_endpoints()

    def __str__(self):
        return 'Chain: {}, {}'.format(self.length, self.open_endpoints)

    def _get_length(self):
        return self.match.end() - self.match.start()

    def _get_open_endpoints(self, empty_value=0):
        open_endpoints = 0
        end_1 = self.match.start() - 1
        if end_1 >= 0 and self.match.string[end_1] == empty_value:
            # not at end and there is no move made
            open_endpoints += 1

        end_2 = self.match.end()
        if end_2 < self.match.endpos and self.match.string[end_2] == empty_value:
            open_endpoints += 1
        return open_endpoints
