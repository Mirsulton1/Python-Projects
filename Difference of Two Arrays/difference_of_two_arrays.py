from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        only_in_nums1 = list(set1 - set2)
        only_in_nums2 = list(set2 - set1)

        return [only_in_nums1, only_in_nums2]

if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,2,3]
    nums2 = [2,4,6]
    print("Output 1: ", sol.findDifference(nums1, nums2))

    nums3 = [1,2,3,3]
    nums4 = [1,1,2,2]
    print("Ouput 2: ", sol.findDifference(nums3, nums4))
