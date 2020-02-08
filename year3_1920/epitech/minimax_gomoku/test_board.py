#!/usr/bin/env python3

import unittest
from board import Board2dArr as Board
from board import Chain


class TestBoardEvaluation(unittest.TestCase):

    # test lines

    def test_row_lines(self):
        B = [[1, 2],
             [3, 4]]
        lines = Board._get_row_lines(B)
        E = [[1, 2], 
             [3, 4]]
        self.assertEqual(lines, E)

    def test_row_lines_num(self):
        B = [[1, 2],
             [3, 4]]
        lines = Board._get_row_lines(B, 1)
        E = [3, 4]
        self.assertEqual(lines, E)

    def test_col_lines(self):
        B = [[1, 2],
             [3, 4]]
        lines = Board._get_col_lines(B)
        E = [[1, 3], 
             [2, 4]]
        self.assertEqual(lines, E)

    def test_col_lines_num(self):
        B = [[1, 2],
             [3, 4]]
        lines = Board._get_col_lines(B, 0)
        E = [1, 3]
        self.assertEqual(lines, E)

    def test_pos_diag_lines(self):
        B = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        lines = Board._get_pos_diag_lines(B) # /
        E = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
        self.assertEqual(lines, E)

    def test_pos_diag_lines_num(self):
        B = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        lines = Board._get_pos_diag_lines(B, 2) # /
        E = [3, 5, 7]
        self.assertEqual(lines, E)

    def test_neg_diag_lines(self):
        B = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        lines = Board._get_neg_diag_lines(B) # \
        E = [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
        self.assertEqual(lines, E)

    def test_neg_diag_lines_num(self):
        B = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        lines = Board._get_neg_diag_lines(B, 3) # \
        E = [2, 6]
        self.assertEqual(lines, E)


    # test chains matching and properties

    @staticmethod
    def str_to_bytes(s):
        return bytearray([int(x) for x in s])

    def test_get_line_matches(self):
        test = '11111101201'
               #01234567890
        spans = [match.span() for match in Board._get_line_matches(1, self.str_to_bytes(test))]
        self.assertEqual(spans, [(0, 5), (5, 6), (7, 8), (10, 11)])

    def test_chain(self):
        test = '0222210'
        match = list(Board._get_line_matches(2, self.str_to_bytes(test)))[0]
        c = Chain(match)
        self.assertEqual(c.length(), 4)
        self.assertEqual(c.open_endpoints(), 1)


    # test updating chain state




if __name__ == '__main__':
    unittest.main()