class Solution:
    def reverse_words(self, s: str) -> str:
        # Step 1: Trim Leading/trailing spaces and split by one or more spaces
        words = s.strip().split()

        # Step 2: Reverse the list of words and join with a single space
        reversed_sentence = ' '.join(reversed(words))

        return reversed_sentence
    
# Example usage
sol = Solution()
print(sol.reverse_words("the sky is blue"))
print(sol.reverse_words("   hello world     "))
print(sol.reverse_words("a good     example"))