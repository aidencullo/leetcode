# 128. Longest Consecutive Sequence
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)  # n time n space
        longest = 0
        for x in seen:  # n + n = O(n) time
            if x - 1 not in seen:  # 1 time
                total = 0
                while x in seen:
                    total += 1
                    x += 1
                longest = max(longest, total)
        return longest
