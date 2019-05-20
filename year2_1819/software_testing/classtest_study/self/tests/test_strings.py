#!/usr/bin/env python3

import unittest
from src.strings import nochange, uppercase, nospace

class StringsTestCase(unittest.TestCase):

    def test_nochange(self):
        s = "h2bh+q"
        self.assertEqual(nochange(s), s, msg="You are not a programmer. Why do I pay you.")

    def test_uppercase(self):
        s = "hello world"
        self.assertEqual(uppercase(s), s.upper(), msg="Test no.2 failed")
        
    def test_not_lowercase(self):
        s = "hello world"
        self.assertNotEqual(uppercase(s), s.lower())

    def test_nospace(self):
        s = "h e ll o "
        self.assertEqual(nospace(s), s.replace(" ", ""))

    def test_uppercase_nospace(self):
        s = "H e ll O  "
        self.assertEqual(nospace(uppercase(s)), s.replace(" ", "").upper())
    
if __name__ == "__main__":
    unittest.main()
