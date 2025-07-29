from successful_pairs import Solution

if __name__ == "__main__":
    spells = list(map(int, input("Enter spells: ").split()))
    potions = list(map(int, input("Enter potions: ").split()))
    success = int(input("Enter success threshold: "))

    sol = Solution()
    result = sol.successfulPairs(spells, potions, success)
    print("Result:", result)
