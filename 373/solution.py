from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from itertools import product
        pairs = product(nums1, nums2)
        pair_sum_kv = [(sum(pair), pair) for pair in pairs]
        pair_sum_kv.sort()
        pairs_k = [pair for (value, pair) in pair_sum_kv]
        return pairs_k[:k]
                   
