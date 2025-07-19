import unittest
from count_goog_nodes import TreeNode, build_tree, goodNodes

class TestGoodNodes(unittest.TestCase):

    def test1(self):
        vals = [3,1,4,3, None, 1, 5]
        root = build_tree(vals)
        self.assertEqual(goodNodes(root), 4)

    def test2(self):
        vals = [3,3,None,4,2]
        root = build_tree(vals)
        self.assertEqual(goodNodes(root), 3)
    
    def test3(self):
        vals = [1]
        root = build_tree(vals)
        self.assertEqual(goodNodes(root), 1)

    def allGood(self):
        vals = [5,5,5,5,5,5,5]
        root = build_tree(vals)
        self.assertEqual(goodNodes(root), 7)

    def allDescending(self):
        vals = [10,9,8,7,6]
        root = build_tree(vals)
        self.assertEqual(goodNodes(root), 1)

    def emptyTree(self):
        self.assertIsNone(build_tree([]))

if __name__ == "__main__":
    unittest.main()