#!/usr/bin/env python3

import unittest
from pbrain_gomoku_ai import (
    commands_re,
)


class TestProtocolCommandsMatching(unittest.TestCase):

    def test_start(self):
        prog = commands_re['start']
        self.assertTrue(prog.match('START 19'))
        self.assertFalse(prog.match('START afda'))

    def test_turn(self):
        prog = commands_re['turn']
        self.assertTrue(prog.match('TURN 19,12'))
        self.assertFalse(prog.match('TURN'))

    def test_begin(self):
        prog = commands_re['begin']
        self.assertTrue(prog.match('BEGIN'))
        self.assertFalse(prog.match(' BEGIN  '))

    def test_board(self):
        prog = commands_re['board']
        self.assertTrue(prog.match('BOARD'))
        self.assertFalse(prog.match('  BOARD'))

    def test_boarddata(self):
        prog = commands_re['boarddata']
        self.assertTrue(prog.match('2,3,1'))
        self.assertTrue(prog.match('2,4,2'))
        self.assertTrue(prog.match('1,1,3'))
        self.assertFalse(prog.match('2,2,5'))

    def test_boarddone(self):
        prog = commands_re['boarddone']
        self.assertTrue(prog.match('DONE'))
        self.assertFalse(prog.match('   DONE  '))

    def test_info(self):
        prog = commands_re['info']
        self.assertTrue(prog.match('INFO timeout_match 300000'))
        self.assertTrue(prog.match('INFO folder D:\gomoku\.piskvork'))
        self.assertFalse(prog.match('INFO key'))

    def test_end(self):
        prog = commands_re['end']
        self.assertTrue(prog.match('END'))
        self.assertFalse(prog.match('END 1'))

    def test_about(self):
        prog = commands_re['about']
        self.assertTrue(prog.match('ABOUT'))
        self.assertFalse(prog.match(' ABOUT  '))


if __name__ == '__main__':
    unittest.main()