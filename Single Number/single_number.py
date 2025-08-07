from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
def main():
    nums = list(map(int, input("Enter integers separated by space: ").split()))
    sol = Solution()
    result = sol.singleNumber(nums)
    print("Single number is:", result)

if __name__ == "__main__":
    main()
