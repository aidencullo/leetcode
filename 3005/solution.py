from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = max(Counter(nums).values())
        return sum(1 for x in nums if cnt[x] == max_freq)
