from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,7,3,6,5,6]
    print("Output 1: ", sol.pivotIndex(nums1))

    nums2 = [1,2,3]
    print("Output 2: ", sol.pivotIndex(nums2))

    nums3 = [2,1,-1]
    print("Output 3: ", sol.pivotIndex(nums3))
