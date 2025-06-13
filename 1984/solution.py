class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = float('inf')
        l, r = 0, k - 1
        n = len(nums)
        while r < n:
            diff = min(diff, nums[r] - nums[l])
            l += 1
            r += 1
        return diff
