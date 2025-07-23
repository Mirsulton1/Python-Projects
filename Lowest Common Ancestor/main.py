from lowest_common_ancestor import Solution, build_tree, find_node

if __name__ == "__main__":
    values = input("Enter tree nodes as a list: ")
    values = [int(x) if x != "null" else None for x in values.strip().split(",")]

    root = build_tree(values)

    p_val = int(input("Enter the value of node p: "))
    q_val = int(input("Enter the value of node q: "))

    p = find_node(root, p_val)
    q = find_node(root, q_val)

    if not p or not q:
        print("One or both nodes not found in the tree.")
    else:
        sol = Solution()
        lca = sol.lowestCommonAncestor(root, p, q)
        print(f"The Lowest Common Ancestor of {p_val} and {q_val} is: {lca.val}")