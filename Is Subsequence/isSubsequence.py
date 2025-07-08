class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move pointer in t
            j += 1      # always move pointer in t

        return i == len(s)  # if we matched all characters in s
    
# Example usage
sol = Solution()
print(sol.is_subsequence("abc", "ahbgdc"))
print(sol.is_subsequence("axc", "ahbgdc"))