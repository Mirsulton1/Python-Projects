from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0

        for change in gain:
            altitude += change  # Update current altitude
            max_altitude = max(max_altitude, altitude)  # Track highest

        return max_altitude

if __name__ == "__main__":
    sol = Solution()

    gain1 = [-5,1,5,0,-7]
    print("Output 1: ", sol.largestAltitude(gain1))

    gain2 = [-4,-3,-2,-1,4,3,2]
    print("Output 2: ", sol.largestAltitude(gain2))