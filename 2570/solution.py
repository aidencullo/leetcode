from collections import defaultdict
from itertools import chain

class Solution:
    def mergeArrays(self, nums1, nums2):
        d = defaultdict(int)
        for k, v in chain(nums1, nums2):
            d[k] += v
        return sorted(d.items())
