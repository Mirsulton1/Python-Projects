from typing import List

class Solution:
    def increasing_triplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num   # update the smallest so far
            elif num <= second:
                second = num  # update the second smallest so far
            else:
                # If we find a number than both -> triplet exists
                return True
        
        return False # no increasing triplet found
    
# Example usage
sol = Solution()
print(sol.increasing_triplet([1, 2, 3, 4, 5]))
print(sol.increasing_triplet([5, 4, 3, 2, 1]))
print(sol.increasing_triplet([2, 1, 5, 0, 4, 6]))