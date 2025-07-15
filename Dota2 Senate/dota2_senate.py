from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        # Fill initial queues with indices of R and D
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate the rounds
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()

            if r_index < d_index:
                # Radiant bans Dire, comes back in next round
                radiant.append(r_index + n)
            else: 
                # Dire bans Radiant, comes back in next round
                dire.append(d_index + n)
            
        # Whoever still has members wins
        return "Radiant" if radiant else "Dire"
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.predictPartyVictory("RD"))
    print(sol.predictPartyVictory("RDD"))
    print(sol.predictPartyVictory("RRDDD"))
    print(sol.predictPartyVictory("DDRRRR"))
