class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the previous and next plots are also empty or out of bounds
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1 # Plant a flower here
                    count += 1
                    if count >= n:
                        return True # Enough flowers planted
        return count >= n
    

# Example usage
sol = Solution()

print(sol.canPlaceFlowers([1,0,0,0,1], 1)) # Output: True
print(sol.canPlaceFlowers([1,0,0,0,1], 2)) # Output: False