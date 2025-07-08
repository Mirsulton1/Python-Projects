from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        # Step 1: Build left products
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Step 2: Multiply with right products (in reverse)
        right = 1
        for i in range(n -1, -1, -1):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer
    
# Example usage
sol = Solution()

# Example 1
result1 = sol.product_except_self([1, 2, 3, 4])
print(result1) # Output: [24, 12, 8, 6]

# Example 2
result2 = sol.product_except_self([-1, 1, 0, -3, 3])
print(result2) # Output: [0, 0, 9, 0, 0]