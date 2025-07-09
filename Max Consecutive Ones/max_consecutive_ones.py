from typing import List

class Solution:
    # method longestOnes, parameteres nums: list of integers, k: max number of 0s we can flip
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Left pointer for the sliding window
        left = 0
        # Stores maximum length of valid subarray found
        max_length = 0
        # Keeps track of zeros in the current window
        zeros = 0

        # Loops through each index from 0 to end
        for right in range(len(nums)):
    
            if nums[right] == 0:
                zeros += 1

            # If we have more than k zeros we need to shrink the window from the left side
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1  # shrink window from left
            
            max_length = max(max_length, right - left + 1)

        return max_length

sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))