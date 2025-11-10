class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        total = 0
        n = len(nums)
        i = n - 1
        while i >= 0 and total <= sum(nums) / 2:
            total += nums[i]
            i -= 1
        return list(reversed(nums[i + 1:]))
