class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        min_stack = []
        LCIS = 1
        current_IS = 0
        last = -math.inf
        for x in nums:
            if last < x:
                current_IS += 1
            else:
                current_IS = 1
            LCIS = max(LCIS, current_IS)
            last = x
        return LCIS
