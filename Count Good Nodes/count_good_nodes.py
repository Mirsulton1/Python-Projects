from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    def DFS(node: TreeNode, max_so_far: int) -> int:
        if not node:
            return 0
        good = 1 if node.val >= max_so_far else 0
        max_so_far = max(max_so_far, node.val)
        return good + DFS(node.left, max_so_far) + DFS(node.right, max_so_far)
    return DFS(root, root.val)

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
