import unittest
from letter_combination import Solution

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            sorted(self.sol.letterCombinations("23")),
            sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        )

    def test_empty(self):
        self.assertEqual(self.sol.letterCombinations(""), [])

    def test_single_digit(self):
        self.assertEqual(
            sorted(self.sol.letterCombinations("2")),
            sorted(["a", "b", "c"])
        )

    def test_longer_input(self):
        result = self.sol.letterCombinations("279")
        self.assertTrue(all(len(s) == 3 for s in result))  # all combinations of length 3

if __name__ == '__main__':
    unittest.main()
