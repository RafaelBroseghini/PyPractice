import unittest
from maths import *


class MathsBeginnerTestCase(unittest.TestCase):
    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(0), 'even')
        self.assertEqual(even_or_odd(1), 'odd')
        self.assertEqual(even_or_odd(-1), 'odd')
        print("\n.Passed 1. alphabet_counter with no errors!")

    def test_sum_them_all(self):
        self.assertEqual(sum_them_all(0), 0)
        self.assertEqual(sum_them_all(5), 15)
        print("Passed 2. alphabet_counter_version_two with no errors!")


if __name__ == "__main__":
    unittest.main()
