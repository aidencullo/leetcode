class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        import math
        longest = -math.inf
        l, r = 0, 0
        n = len(nums)
        while r < n:
            if nums[r] > threshold:
                l, r = r + 1, r + 1
            else:
                r += 1
                longest = max(longest, r - l)
        return longest
