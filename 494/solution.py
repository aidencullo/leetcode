from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def findTargetSumWaysRecursive(index: int, running: int) -> int:
            if index == n and running == target:
                return 1
            if index == n and running != target:
                return 0
            return findTargetSumWaysRecursive(index + 1, running + nums[index]) + findTargetSumWaysRecursive(index + 1, running - nums[index])

        n = len(nums)
        return findTargetSumWaysRecursive(0, 0)
