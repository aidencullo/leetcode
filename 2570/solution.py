from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c = Counter(dict(nums1)) + Counter(dict(nums2))
        lst = [[k, v] for k, v in c.items()]
        return sorted(lst)
