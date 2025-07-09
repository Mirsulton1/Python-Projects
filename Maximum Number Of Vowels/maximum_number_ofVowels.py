class Solution:
    # method maxVowels take string s, and integer k, and return int
    def maxVowels(self, s: str, k: int) -> int:
        # Creates a set of vowels for O(1) lookup
        vowels = set('aeiou')
        # Tracks the maximum vowels seen in any window of size k
        max_count = 0
        # Tracks number of vowels in current window
        current_count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        # Initialize max_count with the count form the first window
        max_count = current_count

        # Slide the window one character at a time
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1 # remove the char going out
            if s[i] in vowels:
                current_count += 1 # add the char coming in
            max_count = max(max_count, current_count)

        return max_count

sol = Solution()
print(sol.maxVowels("abciiidef", 3))
print(sol.maxVowels("aieou", 2))
print(sol.maxVowels("leetcode", 3))
