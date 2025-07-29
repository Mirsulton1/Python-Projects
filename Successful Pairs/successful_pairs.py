from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            threshold = success / spell
            index = bisect_left(potions, threshold)
            res.append(m - index)

        return res
