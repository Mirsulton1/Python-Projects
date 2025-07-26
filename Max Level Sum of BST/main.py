from max_level_sum import Solution, build_tree

def main():
    user_input = input("Enter the tree in level order (comma-separated, use 'null' for missing nodes): ")
    values = [int(val) if val.strip().lower() != 'null' else None for val in user_input.strip().split(',')]

    root = build_tree(values)
    sol = Solution()
    result = sol.maxLevelSum(root)
    print("The level with the maximum sum is:", result)

if __name__ == "__main__":
    main()