class Solution:
    def reverse_vowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU') # Set of vowels (both lowercase and uppercase)
        chars = list(s)            # Convert string to list for easy swapping
        left, right = 0, len(chars) - 1

        while left < right:
            # Move left pointer to the next vowel
            while left < right and chars[left] not in vowels:
                left += 1
            # Move right pointer to the previous vowel
            while left < right and chars[right] not in vowels:
                right -= 1

            # Swap vowels
            chars[left], chars[right] = chars[right], chars[left]

            # Move inward
            left += 1
            right -= 1

        return ''.join(chars)
    
# Example usage
sol = Solution()
print(sol.reverse_vowels("IceCreAm"))
print(sol.reverse_vowels("leetcode"))