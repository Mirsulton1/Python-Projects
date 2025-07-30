import unittest
from find_peak import Solution

class UnitTests(unittest.TestCase):
    def stUp(self):
        self.sol = Solution()

    def test1(self):
        nums = [1, 2, 3, 1]
        result = self.sol.findPeakElement(nums)
        self.assertIn(result, [2])

    def test2(self):
        nums = [1,2,1,3,5,6,4]
        result = self.sol.findPeakElement(nums)
        self.assertIn(result, [1,5])  # 2 and 6 are both peaks

    def test3(self):
        nums = [10]
        result = self.sol.findPeakElement(nums)
        self.assertEqual(result, 0)

    def test4(self):
        nums = [1,2]
        result = self.sol.findPeakElement(nums)
        self.assertEqual(result, 1)

    def test5(self):
        nums = [5,4,3,2,1]
        result = self.sol.findPeakElement(nums)
        self.assertEqual(result, 0)

    def test6(self):
        nums = [1,2,3,4,5]
        result = self.sol.findPeakElement(nums)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()