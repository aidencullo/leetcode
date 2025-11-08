class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        min_stack = []
        LCIS = 1
        for x in nums:
            if min_stack and min_stack[-1] >= x:
                min_stack.clear()
            min_stack.append(x)
            LCIS = max(LCIS, len(min_stack))
        return LCIS
