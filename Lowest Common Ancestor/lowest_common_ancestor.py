from typing import Optional

class TreeNode:
    def __init__ (self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if root is None or root is one of p or q, return root
        if not root or root == p or root == q:
            return root
        
        # Recur for left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return non-null, root is he LCA
        if left and right:
            return root
        
        # If only one side return non-null, that's the LCA
        return left if left else right
    
# Helper fundction to build a tree from a list input
def build_tree(nodes: list) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current  = queue.pop(0)
        if current:
            if i < len(nodes) and nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1
        return root

# Helper function to find a node with a specific value
def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    return left if left else find_node(root.right, val)
