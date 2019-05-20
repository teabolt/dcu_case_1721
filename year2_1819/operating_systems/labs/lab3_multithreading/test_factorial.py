#!/usr/bin/env python3

import unittest
import factorial as fa


class FactorialFunctionTestCase(unittest.TestCase):

	def test_zero_fac(self):
		self.assertEqual(fa.fac(0), 1)

	def test_one_fac(self):
		self.assertEqual(fa.fac(1), 1)

	def test_five_fac(self):
		self.assertEqual(fa.fac(5), 120)

	def test_rec_fac(self):
		self.assertEqual(fa.fac(5), 5*fa.fac(4))

	def test_below_zero_fac(self):
		self.assertEqual(fa.fac(-1), -1)



if __name__ == '__main__':
	unittest.main()
