import math


class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def is_nice(array):
            running = 0
            for x in array:
                if running & x:
                    return False
                running |= x
            return True

        subarrays = []
        n = len(nums)
        longest = -math.inf
        for i in range(n):
            for j in range(i, n):
                subarray = nums[i : j + 1]
                if is_nice(subarray):
                    longest = max(longest, len(subarray))
        return longest
