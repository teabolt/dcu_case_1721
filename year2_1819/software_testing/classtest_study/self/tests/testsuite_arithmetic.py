#!/usr/bin/env python3

import unittest
from test_decimal import DecimalTestCase
from test_add import TestAdd


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DecimalTestCase))
    suite.addTest(unittest.makeSuite(TestAdd))
    
    runner = unittest.TextTestRunner()

    print(runner.run(suite))
    

suite()
