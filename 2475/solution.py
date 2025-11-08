from itertools import combinations
from collections import Counter
from math import prod
from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        left_sum = 0
        right_sum = sum(counter.values())
        count = 0
        for key in counter.keys():
            right_sum -= counter[key]
            count += left_sum * counter[key] * right_sum
            left_sum += counter[key]
        return count
