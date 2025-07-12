from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)  # Step 1: Count occurrences
        freq = list(count.values())  # Step 2: Get the list of frequencies
        return len(freq) == len(set(freq))  # Step 3: Check if all frequencies are uniques
    
if __name__ == "__main__":
    sol = Solution()

    arr = [1,2,2,1,1,3]
    print("Output 1: ", sol.uniqueOccurrences(arr))

    arr2 = [1,2]
    print("Output 2: ", sol.uniqueOccurrences(arr2))

    arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
    print("Output 3: ", sol.uniqueOccurrences(arr3))
