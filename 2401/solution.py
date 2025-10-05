import math

class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        n = len(nums)
        running = 0

        longest = -math.inf
        while right < n:
            while running & nums[right] != 0:
                running ^= nums[left]
                left += 1
            running |= nums[right]
            right += 1
            longest = max(longest, right - left)
        return longest
