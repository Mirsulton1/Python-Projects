from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
    
def main():
    n = int(input("Enter n: "))
    sol = Solution()
    print(sol.countBits(n))

if __name__ == "__main__":
    main()
