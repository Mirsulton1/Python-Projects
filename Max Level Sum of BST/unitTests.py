import unittest
from max_level_sum import Solution, build_tree

class TestMaxLevelSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([1, 7, 0, 7, -8, None, None])
        self.assertEqual(self.sol.maxLevelSum(root), 2)

    def test_example2(self):
        root = build_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])
        self.assertEqual(self.sol.maxLevelSum(root), 2)

    def test_single_node(self):
        root = build_tree([10])
        self.assertEqual(self.sol.maxLevelSum(root), 1)

    def test_multiple_levels(self):
        root = build_tree([5,2,3,1,4,-2,1])
        self.assertEqual(self.sol.maxLevelSum(root), 2)

    def test_all_negative(self):
        root = build_tree([-10,-20,-30,-5,-1])
        self.assertEqual(self.sol.maxLevelSum(root), 3)

if __name__ == "__main__":
    unittest.main()