class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def findTargetSumWaysRecursive(index: int, running: int) -> int:
            if (index, running) in mem:
                return mem[(index, running)]
            if index == n and running == target:
                return 1
            if index == n and running != target:
                return 0
            mem[(index, running)] = findTargetSumWaysRecursive(index + 1, running + nums[index]) + findTargetSumWaysRecursive(index + 1, running - nums[index])
            return mem[(index, running)]

        n = len(nums)
        mem = {}
        return findTargetSumWaysRecursive(0, 0)
