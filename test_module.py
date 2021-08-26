import unittest
from code import solve


# the test case
class UnitTests(unittest.TestCase):
    def one_number(self):
        actual = solve('1')
        expected = "1"
        self.assertEqual(
            actual, expected, '1 -> 1')

        actual = solve('12')
        expected = "1"
        self.assertEqual(
            actual, expected, '887 mus no')
        actual = solve('10')
        expected = "2"
        self.assertEqual(
            actual, expected, '887 mus no')
    def two(self):
        actual = solve('919')
        expected = "3"
        self.assertEqual(
            actual, expected, '1 -> 1')
        actual = solve('-919')
        expected = "3"
        self.assertEqual(
            actual, expected, '1 -> 1')
if __name__ == "__main__":
    unittest.main()
