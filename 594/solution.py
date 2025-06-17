class Solution:
    def findLHS(self, nums: List[int]) -> int:
        def check(i, running):
            if i == len(nums):
                if not running:
                    return 0
                high = max(running)
                low = min(running)
                if high - low == 1:
                    return len(running)
                return 0
            else:
                return max(check(i + 1, running), check(i + 1, running + [nums[i]]))
        return check(0, [])
