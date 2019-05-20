#!/usr/bin/env python3

import unittest
from src.add import add

class TestAdd(unittest.TestCase):

    def test_one_plus_one_is_two(self):
        self.assertEqual(add(1, 1), 2)

    def test_one_plus_one_is_minus_one(self):
        self.assertNotEqual(add(1, 1), -1)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
