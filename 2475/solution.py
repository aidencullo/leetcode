from itertools import combinations
from collections import Counter
from math import prod
from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        nums_unique = set(nums)
        counter = Counter(nums)
        count = 0
        for combo in combinations(nums_unique, 3):
            count += prod(counter[key] for key in combo)
        return count
