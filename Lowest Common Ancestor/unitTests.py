import unittest
from lowest_common_ancestor import Solution, build_tree, find_node

class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        self.assertEqual(self.sol.lowestCommonAncestor(root, p, q).val, 3)

    def test2(self):
        root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 5)
        q = find_node(root, 4)
        self.assertEqual(self.sol.lowestCommonAncestor(root, p, q).val, 5)

    def test3(self):
        root = build_tree([1,2])
        p = find_node(root, 1)
        q = find_node(root, 2)
        self.assertEqual(self.sol.lowestCommonAncestor(root, p, q).val, 1)

if __name__ == "__main__":
    unittest.main()