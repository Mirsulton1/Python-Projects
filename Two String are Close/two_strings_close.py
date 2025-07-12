from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Condition 1: Both words must have the same unique characters
        if set(word1) != set(word2):
            return False
    
        # Condition 2: Frequency multisets must watch
        freq1 = Counter(word1).values()
        freq2 = Counter(word2).values()

        return sorted(freq1) == sorted(freq2)

if __name__ == "__main__":
    sol = Solution()

    print(sol.closeStrings("abc", "bca"))
    print(sol.closeStrings("a", "aa"))
    print(sol.closeStrings("cabbba", "abbccc"))
