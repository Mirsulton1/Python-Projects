class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.removeStars("leet**cod*e"))
    print(sol.removeStars("erase*****"))
    print(sol.removeStars("abc*d*e**"))
