class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        import math

        longest = 0
        l, r = 0, 0
        n = len(nums)
        while r < n:
            while l < n and (nums[l] % 2 or nums[l] > threshold):
                l += 1
            r = l
            while r < n:
                if nums[r] > threshold:
                    l = r + 1
                    r += 1
                    break
                if l != r:
                    if nums[r] % 2 == nums[r - 1] % 2:
                        l += 1
                        break
                longest = max(longest, r - l + 1)
                r += 1
        return longest
