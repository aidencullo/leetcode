class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, 0
        n = len(nums)
        lhs = 0
        while r < n:
            while r < n and nums[r] - nums[l] <= 1:
                r += 1
            if nums[r - 1] - nums[l] == 1:
               lhs = max(lhs, r - l)
            current = nums[l]
            while l < n and nums[l] == current:
                l += 1
        return lhs
