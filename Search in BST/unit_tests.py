import unittest
from search_bst import TreeNode, Solution, build_tree, serialize_tree

class TestSearchBST(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([4,2,7,1,3])
        val = 2
        result = self.sol.searchBST(root, val)
        self.assertEqual(serialize_tree(result), [2, 1, 3])

    def test_example2(self):
        root = build_tree([4,2,7,1,3])
        val = 5
        result = self.sol.searchBST(root, val)
        self.assertIsNone(result)

    def test_single_node(self):
        root = build_tree([5])
        val = 5
        result = self.sol.searchBST(root, val)
        self.assertEqual(serialize_tree(result), [5])

    def test_left_child(self):
        root = build_tree([5,3])
        val = 3
        result = self.sol.searchBST(root, val)
        self.assertEqual(serialize_tree(result), [3])

    def test_right_child(self):
        root = build_tree([5,None,8])
        val = 8
        result = self.sol.searchBST(root, val)
        self.assertEqual(serialize_tree(result), [8])

if __name__ == "__main__":
    unittest.main()
