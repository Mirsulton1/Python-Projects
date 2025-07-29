import unittest
from delete_node import TreeNode, Solution, build_tree, serialize_tree

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        root = build_tree([5,3,6,2,4,None,7])
        key = 3
        result = self.sol.deleteNode(root, key)
        self.assertIn(serialize_tree(result), [
            [5,4,6,2,None,None,7],
            [5,2,6,None,4,None,7]
        ])

    def test2(self):
        root = build_tree([5,3,6,2,4,None,7])
        key = 0
        result = self.sol.deleteNode(root, key)
        self.assertEqual(serialize_tree(result), [5,3,6,2,4,None,7])

    def test3(self):
        root = build_tree([])
        key = 0
        result = self.sol.deleteNode(root, key)
        self.assertEqual(serialize_tree(result), [])

    def test4(self):
        root = build_tree([2,1,3])
        key = 2
        result = self.sol.deleteNode(root, key)
        self.assertIn(serialize_tree(result), [
            [3,1],
            [1,None,3]
        ])

if __name__ == "__main__":
    unittest.main()