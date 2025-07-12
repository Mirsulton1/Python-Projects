from collections import Counter

class Solution:
    def equalPairs(self, grid):
        n = len(grid)

        # Step 1: Store rows as tuples and count their frequency
        row_counter = Counter(tuple(row) for row in grid)

        # Step 2: For each column, check how many time it matches a row
        count = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n)) # extract column as tuple
            count += row_counter[col] # if col exists in rows, add its count

        return count
    
if __name__ == "__main__":
    sol = Solution()

    grid1 = [[3,2,1], [1,7,6], [2,7,7]]
    print("Output 1: ", sol.equalPairs(grid1))

    grid2 = [[3,1,2,2], [1,4,4,5], [2,4,2,2], [2,4,2,2]]
    print("Output 2: ", sol.equalPairs(grid2))
