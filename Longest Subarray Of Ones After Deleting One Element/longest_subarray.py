from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # right - left + 1 is the window length
            # we must delete one element, so subtract 1
            max_len = max(max_len, right - left)
        
        return max_len

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 1, 0, 1]
    print("Output 1:", sol.longestSubarray(nums1))  # Expected: 3

    nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print("Output 2:", sol.longestSubarray(nums2))  # Expected: 5

    nums3 = [1, 1, 1]
    print("Output 3:", sol.longestSubarray(nums3))  # Expected: 2

    nums4 = [0, 0, 0]
    print("Output 4:", sol.longestSubarray(nums4))  # Expected: 0

    nums5 = [1]
    print("Output 5:", sol.longestSubarray(nums5))  # Expected: 0