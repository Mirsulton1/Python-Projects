from typing import Optional, List
from collections import deque
from right_side_view import Solution, build_tree

if __name__ == "__main__":
    try:
        user_input = input("Enter tree nodes in level order (e.g., 1,2,3,null,5,null,4): ")
        # Split input and handle empty or malformed input
        if not user_input.strip():
            print("Error: Empty input provided.")
            exit(1)
        
        values = []
        for x in user_input.strip().split(","):
            x = x.strip()
            if x.lower() == 'null':
                values.append(None)
            else:
                try:
                    values.append(int(x))
                except ValueError:
                    print(f"Error: Invalid input '{x}'. All non-null values must be integers.")
                    exit(1)

        root = build_tree(values)
        sol = Solution()
        result = sol.rightSideView(root)
        print("Right side view of the tree:", result)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")