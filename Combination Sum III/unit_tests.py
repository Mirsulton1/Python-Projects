import unittest
from combination_sum import Solution

class UnitTEsts(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(sorted(self.sol.combinationSum3(3,7)), sorted([[1,2,4]]))

    def test_example2(self):
        self.assertEqual(sorted(self.sol.combinationSum3(3, 9)), sorted([[1, 2, 6], [1, 3, 5], [2, 3, 4]]))

    def test_example3(self):
        self.assertEqual(self.sol.combinationSum3(4, 1), [])

    def test_edge_case(self):
        self.assertEqual(self.sol.combinationSum3(9, 45), [[1,2,3,4,5,6,7,8,9]])

if __name__ == '__main__':
    unittest.main()