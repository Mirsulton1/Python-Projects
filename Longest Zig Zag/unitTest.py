import unittest
from longest_zig_zag import TreeNode, Solution, build_tree

class UnitTests(unittest.TestCase):
    def tes1(self):
        vals = [1, None, 1,1,1, None,None,1,1,None,1,None,None,None,1]
        root = build_tree(vals)
        self.assertEqual(Solution().longestZigZag(root), 3)

    def test2(self):
        vals = [1,1,1,None,1,None,None,1,1,None,1]
        root = build_tree(vals)
        self.assertEqual(Solution().longestZigZag(root), 4)

    def test3(self):
        vals = [1]
        root = build_tree(vals)
        self.assertEqual(Solution().longestZigZag(root), 0)

    def test4(self):
        vals = []
        root = build_tree(vals)
        self.assertEqual(Solution().longestZigZag(root), 0)

    def test_linear_right(self):
        vals = [1,None,2,None,3,None,4]
        root = build_tree(vals)
        self.assertEqual(Solution().longestZigZag(root), 1)

    def test_linear_zigzag(self):
        vals = [1,2,None,None,3,None,4]
        root = build_tree(vals)
        self.assertEqual(Solution().longestZigZag(root), 2)

if __name__ == '__main__':
    unittest.main()