import unittest

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.singleNumber([2,2,1]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.singleNumber([4,1,2,1,2]), 4)

    def test_example3(self):
        self.assertEqual(self.sol.singleNumber([1]), 1)

    def test_large(self):
        arr = list(range(1, 10000)) * 2 + [999999]
        self.assertEqual(self.sol.singleNumber(arr), 999999)

if __name__ == "__main__":
    unittest.main()
