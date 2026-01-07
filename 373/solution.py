from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from itertools import product
        pairs = product(nums1, nums2)
        pair_sum_kv = [(sum(pair), pair) for pair in pairs]
        heapq.heapify(pair_sum_kv)
        pairs_k = heapq.nsmallest(k, arr))  # [1, 3]
        return [pair for (s, pair) in pairs_k]
                   
