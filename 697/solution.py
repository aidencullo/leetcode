from collections import Counter
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_seen = dict()
        counts = defaultdict(int)
        degree = 0
        shortest = 0

        for i, x in enumerate(nums):
            if x not in first_seen:
                first_seen[x] = i
            counts[x] += 1
            if counts[x] > degree:
                degree = counts[x]
                shortest = i - first_seen[x] + 1
            if counts[x] == degree:
                shortest = min(shortest, i - first_seen[x] + 1)
        return shortest
