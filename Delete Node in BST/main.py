from delete_node import Solution, build_tree, serialize_tree

if __name__ == "__main__":
    s = Solution()
    try:
        values = input("Enter BST node in level order: ")
        key = int(input("Enter key to delete: "))
        values = [int(x) if x.strip() != "None" else None for x in values.split(',')]
        root = build_tree(values)
        result = s.deleteNode(root, key)
        print("BST after deletion:", serialize_tree(result))
    except Exception as e:
        print("Error:", e)