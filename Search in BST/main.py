from search_bst import build_tree, Solution, serialize_tree

def main():
    s = input("Enter the tree in level-order (comma-separated, use 'null' for missing nodes): ")
    val = int(input("Enter the value to search: "))

    values = [int(x) if x.strip().lower() != "null" else None for x in s.strip().split(",")]
    root = build_tree(values)

    sol = Solution()
    result_node = sol.searchBST(root, val)

    if result_node:
        print("Subtree rooted at value", val, "is:", serialize_tree(result_node))
    else:
        print("Value not found in the tree.")

if __name__ == "__main__":
    main()