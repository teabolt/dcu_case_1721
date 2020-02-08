#!/usr/bin/env python3

import unittest
from board import ChainsContainer
from board import Chain


test_chain_a = 'chain1'
test_chain_b = 'chain2'



class TestBoardEvaluation(unittest.TestCase):

    def test_add(self):
        chains = ChainsContainer()
        chains.add([test_chain_a], 0, 'horizontal', 3)
        self.assertEqual(chains.data, 
                         [[[(test_chain_a, 3)],[],[],[]],
                          [[],[],[],[]]])

    def test_delete(self):
        chains = ChainsContainer()
        chains.add([test_chain_a], 0, 'horizontal', 0)
        chains.add([test_chain_b], 1, 'horizontal', 0)
        chains.delete(direction='horizontal', number=0)
        chains.add([test_chain_b], 0, 'horizontal', 0)
        chains.delete(player=0, direction='horizontal', number=0)
        self.assertEqual(chains.data,
                         [[[],[],[],[]],
                          [[],[],[],[]]])

    def test_iter(self):
        chains = ChainsContainer()
        chains.add([test_chain_a], 0, 'horizontal', 0)
        chains.add([test_chain_b], 1, 'horizontal', 0)
        self.assertEqual(list(chains.iter_all()),
                         [test_chain_a, test_chain_b])
        self.assertEqual(list(chains.iter_all(player=0)),
                         [test_chain_a])
