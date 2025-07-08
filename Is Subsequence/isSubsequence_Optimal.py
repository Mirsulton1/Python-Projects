from collections import defaultdict
import bisect

class SubsequenceChecker:
    def __init__(self, t: str):
        self.index_map = defaultdict(list)
        for i, char in enumerate(t):
            self.index_map[char].append(i)

    def is_subsequence(self, s: str) -> bool:
        prev_index = -1

        for char in s:
            if char not in self.index_map:
                return False
            
            indices = self.index_map[char]
            # Use bisect_right to find the first index > prev_index
            pos = bisect.bisect_right(indices, prev_index)
            if pos == len(indices):
                return False
            
            prev_index = indices[pos]

        return True
    
# Example usage
t = "ahbgdc"
checker = SubsequenceChecker(t)

print(checker.is_subsequence("abc"))
print(checker.is_subsequence("axc"))
print(checker.is_subsequence("agc"))