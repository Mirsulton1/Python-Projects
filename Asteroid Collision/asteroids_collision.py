class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            # Process current asteroid
            while stack and a < 0 < stack[-1]:
                # Compare sizes
                if stack[-1] < -a: # Top is smaller, it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a: # Both are same size
                    stack.pop()
                break
            else:
                # No collision, safe to add
                stack.append(a)

        return stack
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.asteroidCollision([5,10,-5]))
    print(sol.asteroidCollision([8,-8]))
    print(sol.asteroidCollision([10,2,-5]))
    print(sol.asteroidCollision([-2,-1,1,2]))
