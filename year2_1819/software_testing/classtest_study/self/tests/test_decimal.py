#!/usr/bin/env python3

import unittest
from src.decimals import *

class DecimalTestCase(unittest.TestCase):

       def test_roundup(self):
           d = 3.1453
           self.assertAlmostEqual(roundup(d, 2), d, 2)

       def test_divide(self):
           a = 1
           b = 3
           self.assertNotAlmostEqual(divide(a, b), 0)

       def test_subtract(self):
           a = 2/3
           b = 1/3
           self.assertAlmostEqual(subtract(a, b), 1/3)
           

if __name__ == '__main__':
    unittest.main()
