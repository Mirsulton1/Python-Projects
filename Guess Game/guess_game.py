def guess(num: int) -> int:
    global PICK
    if num > PICK:
        return -1
    elif num < PICK:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result < 0:
                right = mid - 1
            else:
                left = mid + 1
        return -1  # Should not reach here if pick is in [1, n]

if __name__ == "__main__":
    try:
        PICK = None  # Global variable for the picked number
        n = int(input("Enter the upper bound (n): "))
        PICK = int(input("Enter the picked number: "))
        assert 1 <= PICK <= n, "Pick must be in range 1 to n"

        sol = Solution()
        result = sol.guessNumber(n)
        print(f"The guessed number is: {result}")
    except Exception as e:
        print("Error:", e)
