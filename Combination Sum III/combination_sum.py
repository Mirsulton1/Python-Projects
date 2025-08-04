# solution.py
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], total: int):
            if len(path) == k and total == n:
                result.append(path[:])
                return
            if len(path) > k or total > n:
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
        
        backtrack(1, [], 0)
        return result
