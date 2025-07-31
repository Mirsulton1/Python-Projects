from letter_combination import Solution

def main():
    digits = input("Enter digits (2-9): ").strip()
    sol = Solution()
    combinations = sol.letterCombinations(digits)
    print("Possible letter combinations:")
    print(combinations)

if __name__ == "__main__":
    main()