import unittest
from right_side_view import Solution, build_tree

class TestRightSideView(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([1,2,3,None,5,None,4])
        self.assertEqual(self.sol.rightSideView(root), [1, 3, 4])

    def test_example2(self):
        root = build_tree([1,2,3,4,None,None,None,5])
        self.assertEqual(self.sol.rightSideView(root), [1, 3, 4, 5])

    def test_example3(self):
        root = build_tree([1,None,3])
        self.assertEqual(self.sol.rightSideView(root), [1, 3])

    def test_empty(self):
        root = build_tree([])
        self.assertEqual(self.sol.rightSideView(root), [])

    def test_single_node(self):
        root = build_tree([7])
        self.assertEqual(self.sol.rightSideView(root), [7])

if __name__ == "__main__":
    unittest.main()