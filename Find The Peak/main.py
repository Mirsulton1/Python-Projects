from find_peak import Solution

def main():
    nums = list(map(int, input("Enter number separated by space: ").split()))
    sol = Solution()
    peak_index = sol.findPeakElement(nums)
    print(f"Peak element index: {peak_index}")
    print(f"Peak element valu: {nums[peak_index]}")

if __name__ == "__main__":
    main()