from typing import List

class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        insert_pos = 0

        # Step 1: Move all non-zero elements forward
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Step 2: Fill the rest of the array with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

# Example usage
sol = Solution()

nums1 = [0, 1, 0, 3, 12]
sol.move_zeroes(nums1)
print("After move_zeroes:", nums1)

nums2 = [0]
sol.move_zeroes(nums2)
print("Aster move_zeroes:", nums2)