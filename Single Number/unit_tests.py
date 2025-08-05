import unittest
from single_number import Solution

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.countBits(2), [0,1,1])

    def test2(self):
        self.assertEqual(self.sol.countBits(5), [0,1,1,2,1,2])

    def test3(self):
        self.assertEqual(self.sol.countBits(0), [0])

    def test4(self):
        self.assertEqual(len(self.sol.countBits(100000)), 100001)

if __name__ == "__main__":
    unittest.main()
