from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1, nums2):
        d = defaultdict(int)
        for arr in (nums1, nums2):
            for k, v in arr:
                d[k] += v
        return sorted(d.items())


"""

uhhhh

lets see line by line

constant
constant (2) == allocate space for new tuple/iterable
m+n to iterate
constant assignment of value

m+n lg m+n

"""
