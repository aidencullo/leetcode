from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def rob(i):
            if i >= n:
                return 0
            value = nums[i]
            leave = rob(i + 1)
            take = value + rob(i + 2)
            return max(leave, take)

        n = len(nums)
        return rob(0)
