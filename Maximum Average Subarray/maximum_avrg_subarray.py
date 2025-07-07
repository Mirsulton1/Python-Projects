from typing import List

class Solution:
    # Takes a list of integeres [nums], takes an integer k, returns float
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculates the sum of the first k elements, this will be the sum of the first sliding window
        current_sum = sum(nums[:k])
        # Initializes max_sum to be equal to current_sum
        max_sum = current_sum

        # Loop starts from index k to the end of the list
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i] # removes left element, add element on right
            # Updates max_sum if the new current_sum if greater than the previous
            max_sum = max(max_sum, current_sum)

        # Return average
        return max_sum / k

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
print(sol.findMaxAverage([5], 1))