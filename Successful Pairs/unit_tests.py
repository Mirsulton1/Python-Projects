import unittest
from successful_pairs import Solution

class TestSuccessfulPairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        spells = [5,1,3]
        potions = [1,2,3,4,5]
        success = 7
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [4,0,3])

    def test_example2(self):
        spells = [3,1,2]
        potions = [8,5,8]
        success = 16
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [2,0,2])

    def test_all_successful(self):
        spells = [10, 20]
        potions = [10, 10]
        success = 50
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [2, 2])

    def test_all_fail(self):
        spells = [1, 1]
        potions = [1, 1]
        success = 10
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [0, 0])

    def test_large_input(self):
        spells = [100000] * 100
        potions = [100000] * 100
        success = 1000000000
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [100]*100)

if __name__ == "__main__":
    unittest.main()
