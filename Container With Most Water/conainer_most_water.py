from typing import List

class Solution:
    def max_area(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])  # height is limited by the shorter line
            w = right - left                      # width is the distance betweeen lines
            max_area = max(max_area, h * w)       # update max area if this one is bigger

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage
sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.max_area(height))