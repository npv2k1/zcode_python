import unittest
from code import solve


# the test case
class UnitTests(unittest.TestCase):
    def one_number(self):
        actual = solve('100')
        expected = "-1"
        self.assertEqual(
            1, 2, '1 -> 1')

        actual = solve('999')
        expected = "-1"
        self.assertEqual(
            actual, expected, '887 mus no')

    def two(self):
        actual = solve('345')
        expected = "354"
        self.assertEqual(
            actual, expected, '1 -> 1')
        actual = solve('-919')
        expected = "3"
        self.assertEqual(
            actual, expected, '1 -> 1')


    # def other(self):
    #     actual = solve('991469126')
    #     expected = "991466129"
    #     self.assertEqual(
    #         actual, expected, '1 -> 1')
if __name__ == "__main__":
    unittest.main()
