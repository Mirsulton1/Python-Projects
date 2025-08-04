from combination_sum import Solution

def main():
    k = int(input("Enter value for k: "))
    n = int(input("enter value for n: "))
    sol = Solution()
    combinations = sol.combinationSum3(k, n)
    print("Valid combinations:")
    print(combinations)

if __name__ == "__main__":
    main()