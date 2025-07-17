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

        if index < len(level_order) and level_order[index] is not None:
            node.left = TreeNode(level_order[index])
            queue.append(node.left)
        index += 1

        if index < len(level_order) and level_order[index] is not None:
            node.right = TreeNode(level_order[index])
            queue.append(node.right)
        index += 1

    return root

def get_leaf_sequence(node, leaf_list):
    if not node:
        return
    if not node.left and not node.right:
        leaf_list.append(node.val)
    get_leaf_sequence(node.left, leaf_list)
    get_leaf_sequence(node.right, leaf_list)

def leafSimilar(root1, root2):
    leaves1 = []
    leaves2 = []
    get_leaf_sequence(root1, leaves1)
    get_leaf_sequence(root2, leaves2)
    return leaves1 == leaves2

def main():
    input1 = input("Enter root1 as level-order (comma-separated, 'null' for None): ")
    input2 = input("Enter root2 as level-order (comma-separated, 'null' for None): ")

    list1 = [int(x) if x != 'null' else None for x in input1.strip().split(',')]
    list2 = [int(x) if x != 'null' else None for x in input2.strip().split(',')]

    root1 = build_tree_from_list(list1)
    root2 = build_tree_from_list(list2)

    result = leafSimilar(root1, root2)
    print("Are the trees leaf-similar?", result)

if __name__ == "__main__":
    main()
