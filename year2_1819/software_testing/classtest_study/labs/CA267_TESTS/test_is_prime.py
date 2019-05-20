import unittest
from code.primes import is_prime

class PrimesTestCase(unittest.TestCase):

    def test_is_five_prime(self):
        self.assertTrue(is_prime(7))

    def test_is_four_prime(self):
        self.assertFalse(is_prime(6))

    def test_is_three_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_two_prime(self):
        self.assertTrue(is_prime(2))

    def test_is_one_prime(self):
        self.assertFalse(is_prime(1))

    def test_is_outofrange_prime(self):
        self.assertFalse(is_prime(0))

    def test_is_negative_prime(self):
        self.assertFalse(is_prime(-5))


                   
if __name__ == '__main__':
    unittest.main()

        
