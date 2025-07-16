from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(level_order):
    if not level_order or level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    index = 1

    while queue and index < len(level_order):
        node = queue.popleft()

        # Left child
        if index < len(level_order) and level_order[index] is not None:
            node.left = TreeNode(level_order[index])
            queue.append(node.left)
        index += 1

        # Right child
        if index < len(level_order) and level_order[index] is not None:
            node.right = TreeNode(level_order[index])
            queue.append(node.right)
        index += 1

    return root

def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)

def main():
    input_str = input("Enter the tree nodes in level order (use 'null' for None): ")
    
    # Replace spaces with commas, then split on comma
    input_str = input_str.replace(" ", ",")
    
    # Convert to list, treating 'null' as None
    input_list = [int(x) if x != 'null' else None for x in input_str.strip().split(',')]

    root = build_tree_from_list(input_list)
    depth = maxDepth(root)

    print("Maximum Depth of Binary Tree:", depth)

if __name__ == "__main__":
    main()
