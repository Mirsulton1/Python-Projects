import unittest
from typing import Optional
from path_sum import TreeNode, Solution  # Import both TreeNode and Solution from path_sum.py

class TestPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test case with an empty tree"""
        self.assertEqual(self.solution.pathSum(None, 0), 0)
        self.assertEqual(self.solution.pathSum(None, 5), 0)

    def test_single_node(self):
        """Test case with a single node tree"""
        root = TreeNode(5)
        self.assertEqual(self.solution.pathSum(root, 5), 1)
        self.assertEqual(self.solution.pathSum(root, 0), 0)
        self.assertEqual(self.solution.pathSum(root, 10), 0)

    def test_binary_tree_with_multiple_paths(self):
        """Test case with multiple valid paths"""
        # Tree:
        #      10
        #     /  \
        #    5   -3
        #   / \    \
        #  3   2    11
        # / \   \
        # 3 -2   1
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)
        
        self.assertEqual(self.solution.pathSum(root, 8), 3)  # Paths: [5,3], [5,3,-2], [-3,11]

    def test_negative_target_sum(self):
        """Test case with negative target sum"""
        # Tree:
        #      1
        #     / \
        #   -2   3
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.right = TreeNode(3)
        
        self.assertEqual(self.solution.pathSum(root, -1), 1)  # Path: [1,-2]

    def test_no_valid_paths(self):
        """Test case with no paths summing to target"""
        # Tree:
        #      1
        #     / \
        #    2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        self.assertEqual(self.solution.pathSum(root, 10), 0)

    def test_linear_tree(self):
        """Test case with a linear tree (single path)"""
        # Tree:
        #      1
        #     /
        #    2
        #   /
        #  3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        self.assertEqual(self.solution.pathSum(root, 6), 1)  # Path: [1,2,3]
        self.assertEqual(self.solution.pathSum(root, 3), 2)  # Paths: [1,2], [3]

if __name__ == '__main__':
    unittest.main()