class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        lhs = 0
        for key in counter:
            if key + 1 in counter:
                lhs = max(lhs, counter[key] + counter[key + 1])
        return lhs
