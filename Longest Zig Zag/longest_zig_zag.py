from typing import Optional
import json

# TreeNode class to define each node in the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node: Optional[TreeNode], is_left: bool, length: int):
            if not node:
                return
            # Update maximum ZigZag length seen so far
            self.max_length = max(self.max_length, length)
            if is_left:
                # Go right (alternate), reset length if going same direction
                dfs(node.right, False, length + 1)
                dfs(node.left, True, 1)
            else:
                # Go left (alternate), reset length if going same direction
                dfs(node.left, True, length + 1)
                dfs(node.right, False, 1)

        # Start DFS from root, trying both directions
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.max_length

# Helper to build binary tree from level-order list input
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Main input interface
def main():
    print("Enter binary tree in level-order list format:")
    print("Example: [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]")
    input_str = input("Tree: ")
    # Wrap the input string in square brackets to make it a valid JSON array
    json_input = f"[{input_str}]"
    try:
        target = json.loads(json_input)
        root = build_tree(target)
        sol = Solution()
        print("Longest ZigZag Path Length:", sol.longestZigZag(root))
    except json.JSONDecodeError as e:
        print(f"Error: Invalid input format. {e}")
        print("Please provide input in the format: 1,null,1,1,1,null,null,1,1,null,1,null,null,null,1")

if __name__ == "__main__":
    main()
