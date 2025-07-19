from typing import Optional
from collections import defaultdict
import unittest

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Dictionary to store prefix sums and their counts
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1 # Base case: one way to have sum = 0

        def DFS (node, current_sum):
            if not node:
                return 0
            
            # Add current node's value to the running sum
            current_sum += node.val

            # Count the number of valid paths ending at the current node
            num_paths = prefix_sum_count([current_sum - targetSum])

            # Update the prefix_sum_count with the current sum
            prefix_sum_count[current_sum] += 1

            # Recurse left and right
            num_paths += DFS(node.left, current_sum)
            num_paths += DFS(node.right, current_sum)

            # Backtrack: remove current_sum from map to not affect other branches
            prefix_sum_count[current_sum] -= 1

            return num_paths
        
        return DFS(root, 0)
