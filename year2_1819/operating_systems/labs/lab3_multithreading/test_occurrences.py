#!/usr/bin/env python3

import unittest
from occurrences import occurs_count


class OccursCountTestCase(unittest.TestCase):

    def test_count(self):
        self.assertEqual(occurs_count('hello', 'l'), 2)

    def test_no_occurrence(self):
        self.assertEqual(occurs_count('goodbye', 'i'), 0)

    def test_all_occur(self):
        s = 'aaaaaaa'
        self.assertEqual(occurs_count(s, 'a'), len(s))


def main():
    unittest.main()


if __name__ == '__main__':
    main()